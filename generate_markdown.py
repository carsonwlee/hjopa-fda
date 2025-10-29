import pandas as pd
import yaml

def get_weighting_rationale():
    """Generate human-readable explanation of the physics-first weighting approach."""
    return """## Weighting Rationale: Physics-First Approach to Runway Excursion Prevention

The scoring weights in this system are not arbitrary—they reflect a **physics-first approach** grounded in three key pillars: historical HondaJet accident data, fundamental physical relationships, and aircraft-specific design limitations. This ensures the scoring system prioritizes factors that directly contribute to preventing runway excursions.

### Why This Approach Matters

Runway excursions represent the most significant landing risk for the HondaJet. Our weighting system addresses this by heavily emphasizing the factors that have been statistically linked to the majority of HondaJet runway excursions, while accounting for the physical relationships that make speed errors exponentially dangerous.

### Key Principles

1. **Historical Data Priority**: Factors linked to actual HondaJet runway excursions receive higher weights
2. **Physical Relationships**: Factors with quadratic relationships (speed² effects) are weighted more heavily due to their exponential impact
3. **Aircraft-Specific Design**: HondaJet limitations (no thrust reversers, limited ground spoilers) amplify the importance of energy management
4. **Direct vs. Indirect Impact**: Measurements at critical points (threshold/touchdown) are weighted higher than predictive stability metrics

### Why Airspeed Gets the Highest Weights (16-18% at threshold, 14-16% at touchdown)

**Historical Evidence**: Excessive airspeed has been identified as a primary factor in nearly all HondaJet runway excursions. Pilots often add unnecessary speed to VREF calculations, which becomes increasingly problematic closer to touchdown.

**Physics: The Exponential Penalty**

Speed errors create a compounding problem due to quadratic relationships:

- **Kinetic Energy**: Doubles with only a ~41% speed increase (KE = ½mv²)
  - Example: +10 kt over VREF (at ~108 kt) = ~19% more energy to dissipate
  - The brakes must absorb this additional energy, requiring more runway

- **Lift**: Also grows quadratically with speed (L = ½ρV²SCL)
  - More lift = less weight on wheels = less braking force available
  - Touchdown at higher speeds occurs at lower angle of attack, reducing ability to dump lift by lowering the nose
  - This prolongs ground roll and reduces stopping effectiveness

- **The Double Penalty**: Excess speed means you have:
  1. More energy to dissipate (kinetic energy)
  2. Less ability to dissipate it (reduced braking force from residual lift)

**Aircraft-Specific Amplification**: Without thrust reversers and with limited ground spoilers (Elite II only, partial coverage), the HondaJet relies heavily on brake effectiveness. Excess speed directly compromises this critical deceleration method.

### Why Touchdown Position and Runway Remaining Matter (12-14%)

Second only to airspeed, these factors directly determine whether sufficient runway remains to stop safely:

- **Touchdown Distance from Threshold (12-13%)**: Early touchdown maximizes available runway length for deceleration. Late touchdown, especially when combined with excess speed, severely limits safety margins.

- **Runway Remaining at Touchdown (13-14%)**: This is a direct outcome measurement—how much runway is left when the aircraft touches down. With brake-limited deceleration, every foot counts.

These factors interact: being high or fast over the threshold directly affects touchdown position, which on shorter runways can be decisive in avoiding an excursion.

### Why Stability Metrics Are Weighted Lower (2-3%)

Stability metrics like "Airspeed consistent" and "Vertical speed consistent" receive lower weights (typically 2%) not because they're unimportant, but because they serve a **predictive/supporting role** rather than being direct measurements of excursion risk.

- They provide early warning of potential problems
- Statistical correlation shows that unstable approaches lead to poorer threshold performance
- However, the physics of excursion risk hinge on conditions **at the threshold and touchdown**, not earlier in the approach
- These metrics support the primary factors by helping ensure pilots reach the threshold in a controlled state

### Why Navigation/Procedural Items Are Weighted Minimally (1-2%)

Items like ILS glideslope deviation, localizer deviation, and crossing altitudes receive minimal weights (1-2%) because:

- They are important for procedural compliance and training
- However, they have not been statistically prominent as primary causes in HondaJet excursion data
- They contribute indirectly to safety but don't directly measure the energy management factors that drive excursion risk
- Every item still receives at least minimal weight to ensure comprehensive coverage

### Weight Distribution Summary

**Instrument Approaches**:
- **Airspeed metrics**: 42% total (cumulative across approach phases, with highest at threshold/touchdown)
- **Touchdown/runway factors**: 25% (touchdown distance + runway remaining)
- **Critical factors combined**: 67% of total weight on the highest-risk elements

**Visual Approaches**:
- **Airspeed metrics**: 50% total (even higher emphasis due to lack of glideslope guidance)
- **Touchdown/runway factors**: 27% 
- **Critical factors combined**: 77% of total weight

All weight categories total 100%, ensuring complete scoring coverage while prioritizing factors with the greatest impact on runway safety.

### Operational Implications

This weighting structure guides pilots toward:
- **Tight speed control** at threshold and touchdown (no speed additions to VREF)
- **Early touchdown** to maximize runway for brake-limited stopping
- **Go-around decisions** if conditions at 50' AGL or threshold are not ideal
- **Awareness** that small speed errors create exponential energy increases

The weights aren't just numbers—they reflect real physics, real aircraft limitations, and real historical outcomes. When the system emphasizes airspeed control heavily, it's because physics and accident data tell us that's where the biggest risk lies.

---

*This weighting rationale is based on historical HondaJet excursion data, fundamental aerodynamic and kinetic energy relationships, and the aircraft's specific design constraints. For technical details on the weighting methodology, see `LLM_Scoring_Guidance.md`.*

---
"""

def create_markdown_table(group_df, desired_order):
    available_columns = [col for col in desired_order if col in group_df.columns]
    filtered_df = group_df[available_columns]
    # Fill NaN values with 'N/A'
    filtered_df = filtered_df.fillna('N/A')
    return filtered_df.to_markdown(index=False)

def main():
    # Load the YAML file
    yaml_file = 'HJOPA-Scoring-FDA.yml'
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    df = pd.DataFrame(yaml_data)
    
    # Start with title and rationale
    markdown_output = "# HJOPA - HondaJet Flight Scoring Envelope\n\n"
    markdown_output += get_weighting_rationale() + "\n"

    desired_order = ['Evaluate', 'Weight', 'Tolerance Lower', 'Tolerance Upper', 
                     'Tolerance Unit', 'Evaluate lower limit', 'Evaluate upper limit', 'Evaluation Unit']

    for group in df['Group'].unique():
        group_df = df[df['Group'] == group]
        if group == 'Overall Weights':
            # Only use 'Evaluate' and 'Weight' columns for 'Overall Weights'
            markdown_table = create_markdown_table(group_df, ['Evaluate', 'Weight'])
            markdown_output += f"## {group}\n\n{markdown_table}\n\n"
        elif group == 'Flight Data Analysis':
            # Create a new DataFrame for 'Flight Data Analysis'
            flight_data_df = pd.DataFrame()
            flight_data_df['All'] = group_df['Flight Rules'].apply(lambda x: 'x' if x == 'All' else '')
            flight_data_df['VFR'] = group_df['Flight Rules'].apply(lambda x: 'x' if x == 'VFR' else '')
            flight_data_df['IFR'] = group_df['Flight Rules'].apply(lambda x: 'x' if x == 'IFR' else '')
            flight_data_df['Evaluate'] = group_df['Evaluate']
            flight_data_df['Caution Lower'] = group_df['Caution Lower'] if 'Caution Lower' in group_df.columns else None
            flight_data_df['Caution Upper'] = group_df['Caution Upper'] if 'Caution Upper' in group_df.columns else None
            flight_data_df['Unit'] = group_df['Unit']
            markdown_table = flight_data_df.to_markdown(index=False)
            markdown_output += f"## {group}\n\n{markdown_table}\n\n"
        elif group == 'Standard Operating Parameters':
            # Create a markdown table for 'Standard Operating Parameters'
            markdown_table = create_markdown_table(group_df, ['Characteristic', 'Value'])
            markdown_output += f"## {group}\n\n{markdown_table}\n\n"
        elif 'Segment Group' in group_df.columns:
            for segment_group in group_df['Segment Group'].unique():
                segment_group_df = group_df[group_df['Segment Group'] == segment_group]
                markdown_table = create_markdown_table(segment_group_df, desired_order)
                markdown_output += f"## {group}\n### {segment_group}\n\n{markdown_table}\n\n"
        else:
            markdown_table = create_markdown_table(group_df, desired_order)
            markdown_output += f"## {group}\n\n{markdown_table}\n\n"

    # Save the output to a Markdown file
    with open('README.md', 'w') as md_file:
        md_file.write(markdown_output)
if __name__ == "__main__":
    main()