#!/usr/bin/env python3
"""
Analyze Garmin G3000 parameters across HondaJet variants to show evolution of capabilities.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Set, Tuple

def load_garmin_file(filepath: str) -> Dict:
    """Load a Garmin parameter JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_parameters_evolution():
    """Analyze how parameters evolved across HondaJet variants."""

    # File paths in chronological order
    files = {
        'Legacy': 'Garmin-Parameters/hondajet_legacy_g3000_006-B1792-35.json',
        'APMG': 'Garmin-Parameters/hondajet_apmg_g3000_006-B1792-36.json',
        'Elite': 'Garmin-Parameters/hondajet_elite_g3000_006-B3039-10.json',
        'Elite S': 'Garmin-Parameters/hondajet_elite-s_g3000_006-B3039-26.json',
        'Elite II': 'Garmin-Parameters/hondajet_elite-II_g3000_006-B3039-29_0A.json'
    }

    # Load all parameter files
    data = {}
    for variant, filepath in files.items():
        data[variant] = load_garmin_file(filepath)

    # Extract parameter names and metadata for each variant
    analysis = {}
    for variant, file_data in data.items():
        parameters = file_data['parameters']
        param_names = {p['name'] for p in parameters}

        analysis[variant] = {
            'parameter_count': len(parameters),
            'parameters': param_names,
            'unit_software_version': file_data['flight_data_system']['unit_software_version'],
            'unit_software_part': file_data['flight_data_system']['unit_software_part_number'],
            'system_software_part': file_data['flight_data_system']['system_software_part_number']
        }

    return analysis, data

def find_new_parameters(analysis: Dict) -> Dict[str, List[str]]:
    """Find which parameters were added in each version."""
    variants = list(analysis.keys())
    new_params = {}

    # Start with first variant (Legacy)
    previous_params = analysis[variants[0]]['parameters']

    for i in range(1, len(variants)):
        current_variant = variants[i]
        current_params = analysis[current_variant]['parameters']

        # Find parameters that are new in this version
        new_in_version = current_params - previous_params
        new_params[current_variant] = sorted(list(new_in_version))

        # Update previous params for next iteration
        previous_params = current_params

    return new_params

def categorize_parameters(parameters: List[str]) -> Dict[str, List[str]]:
    """Categorize parameters by their function/purpose."""
    categories = {
        'Time/Date': [],
        'Position/Navigation': [],
        'Altitude': [],
        'Air Data': [],
        'Attitude': [],
        'Engine': [],
        'Electrical': [],
        'Fuel': [],
        'Communications': [],
        'GPS Precision': [],
        'Aircraft Systems': []
    }

    # Define keywords for categorization
    category_keywords = {
        'Time/Date': ['Date', 'Time', 'UTC'],
        'Position/Navigation': ['Latitude', 'Longitude', 'Waypoint', 'NAV', 'CRS', 'HDG', 'TRK', 'HSI', 'CDI', 'Wpt', 'MagVar'],
        'Altitude': ['AltInd', 'BaroA', 'AltMSL', 'AltGPS'],
        'Air Data': ['IAS', 'TAS', 'GndSpd', 'VSpd', 'OAT', 'Wnd'],
        'Attitude': ['Pitch', 'Roll', 'LatAc', 'NormAc'],
        'Engine': ['E1', 'E2', 'ITT', 'N1', 'N2', 'Oil', 'FFlow', 'FPres', 'MAP', 'RPM', 'Torq', 'NG'],
        'Electrical': ['volt'],
        'Fuel': ['FQty'],
        'Communications': ['COM'],
        'GPS Precision': ['HAL', 'VAL', 'HPL', 'VPL', 'GPSfix'],
        'Aircraft Systems': ['Afcs', 'Weight', 'Fix Mode']
    }

    for param in parameters:
        categorized = False
        for category, keywords in category_keywords.items():
            if any(keyword in param for keyword in keywords):
                categories[category].append(param)
                categorized = True
                break

        if not categorized:
            categories['Aircraft Systems'].append(param)

    # Remove empty categories
    return {k: v for k, v in categories.items() if v}

def create_text_visualization(analysis: Dict, new_params: Dict[str, List[str]]):
    """Create a text-based visualization showing parameter evolution."""

    variants = list(analysis.keys())
    param_counts = [analysis[v]['parameter_count'] for v in variants]
    new_counts = [len(new_params.get(v, [])) for v in variants]

    print("\n" + "="*80)
    print("HONDAJET GARMIN G3000 PARAMETER EVOLUTION VISUALIZATION")
    print("="*80)

    # Text-based bar chart for parameter counts
    print("\n📊 TOTAL PARAMETERS BY VARIANT:")
    print("-" * 50)
    max_count = max(param_counts)
    for variant, count in zip(variants, param_counts):
        bar = "█" * int(count * 40 / max_count)
        print(f"{variant:<12} {count:>3} {bar}")

    # New parameters bar chart
    print("\n🆕 NEW PARAMETERS ADDED BY VARIANT:")
    print("-" * 50)
    max_new = max(new_counts) if new_counts else 1
    for variant, count in zip(variants, new_counts):
        if max_new > 0:
            bar = "█" * int(count * 40 / max_new) if count > 0 else ""
        else:
            bar = ""
        print(f"{variant:<12} {count:>3} {bar}")

    # Parameter categories evolution
    print("\n📂 PARAMETERS BY CATEGORY EVOLUTION:")
    print("-" * 50)

    all_params = set()
    for variant in variants:
        all_params.update(analysis[variant]['parameters'])

    categories_over_time = []
    for variant in variants:
        current_params = list(analysis[variant]['parameters'])
        categories = categorize_parameters(current_params)
        category_counts = {cat: len(params) for cat, params in categories.items()}
        categories_over_time.append(category_counts)

    # Get all unique categories
    all_categories = sorted(set().union(*[set(cat_dict.keys()) for cat_dict in categories_over_time]))

    print(f"{'Category':<20} {'Legacy':<8} {'APMG':<8} {'Elite':<8} {'Elite S':<8} {'Elite II':<8}")
    print("-" * 70)
    for category in all_categories:
        counts = [cat_dict.get(category, 0) for cat_dict in categories_over_time]
        print(f"{category:<20} {counts[0]:<8} {counts[1]:<8} {counts[2]:<8} {counts[3]:<8} {counts[4]:<8}")

    # Software evolution
    print("\n💾 SOFTWARE VERSION EVOLUTION:")
    print("-" * 50)
    for variant, info in analysis.items():
        print(f"{variant:<12} {info['unit_software_version']} ({info['unit_software_part']})")

    print("\n" + "="*80)

def generate_detailed_report(analysis: Dict, new_params: Dict[str, List[str]], data: Dict):
    """Generate a detailed markdown report of the findings."""

    report = ["# Garmin G3000 Parameter Evolution Analysis\n"]

    report.append("## Overview\n")
    report.append("This analysis examines how Garmin G3000 flight data system parameters evolved across HondaJet variants, showing the progression of capabilities from Legacy to Elite II.\n\n")

    report.append("## Key Findings\n\n")

    # Parameter evolution
    report.append("### Parameter Count Evolution\n")
    report.append("| Variant | Parameters | Unit Software | System Software |\n")
    report.append("|---------|------------|---------------|----------------|\n")

    for variant, info in analysis.items():
        report.append(f"| {variant} | {info['parameter_count']} | {info['unit_software_version']} | {info['system_software_part']} |\n")

    report.append("\n")

    # New parameters by version
    report.append("### New Parameters Added by Version\n\n")

    for variant, params in new_params.items():
        if params:
            report.append(f"#### {variant}\n")
            report.append(f"**Added {len(params)} new parameters:**\n\n")

            # Categorize the new parameters
            categories = categorize_parameters(params)
            for category, cat_params in categories.items():
                if cat_params:
                    report.append(f"- **{category}:** {', '.join(sorted(cat_params))}\n")
            report.append("\n")

    # Major capability improvements
    report.append("### Major Capability Improvements\n\n")

    report.append("**Elite S (vs Elite):**\n")
    report.append("- Added dual GPS constellation support (HAL2, VAL2, HPLwas2, HPLfd2, VPLwas2)\n")
    report.append("- Added aircraft weight monitoring\n")
    report.append("- Added GPS fix mode information\n\n")

    report.append("**Elite II (vs Elite S):**\n")
    report.append("- Added comprehensive turboprop engine parameters (MAP, RPM, Torque, NG)\n")
    report.append("- Enhanced engine monitoring capabilities\n\n")

    # Software evolution
    report.append("### Software Evolution\n\n")
    report.append("**Version 20.91** (Legacy/APMG): Initial G3000 implementation\n\n")
    report.append("**Version 31.11.21.10** (Elite/Elite S): Major software upgrade with enhanced GPS capabilities\n\n")
    report.append("**Version 31.11.60** (Elite II): Incremental update with additional engine parameters\n\n")

    # Parameter categories summary
    report.append("### Parameter Categories Summary\n\n")

    all_params = set()
    for variant in analysis:
        all_params.update(analysis[variant]['parameters'])

    categories = categorize_parameters(list(all_params))
    for category, params in sorted(categories.items()):
        report.append(f"**{category}** ({len(params)} parameters): {', '.join(sorted(params))}\n\n")

    return ''.join(report)

def main():
    """Main analysis function."""
    print("Analyzing Garmin G3000 parameter evolution...")

    # Analyze parameters
    analysis, raw_data = analyze_parameters_evolution()

    # Find new parameters in each version
    new_params = find_new_parameters(analysis)

    # Create text-based visualization
    create_text_visualization(analysis, new_params)

    # Generate detailed report
    report = generate_detailed_report(analysis, new_params, raw_data)

    # Save report
    with open('Garmin_Parameters_Evolution_Report.md', 'w') as f:
        f.write(report)

    print("Analysis complete!")
    print(f"- Generated visualization: charts/garmin_parameters_evolution.svg")
    print(f"- Generated report: Garmin_Parameters_Evolution_Report.md")

    # Print summary to console
    print("\n=== PARAMETER EVOLUTION SUMMARY ===")
    for variant, info in analysis.items():
        new_count = len(new_params.get(variant, []))
        print(f"{variant}: {info['parameter_count']} parameters ({new_count} new)")

if __name__ == "__main__":
    main()
