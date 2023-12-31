import pandas as pd
import yaml

def create_markdown_table(group_df, desired_order):
    available_columns = [col for col in desired_order if col in group_df.columns]
    filtered_df = group_df[available_columns]
    # Fill NaN values with 'N/A'
    filtered_df = filtered_df.fillna('N/A')
    return filtered_df.to_markdown(index=False)

def main():
    # Load the YAML file
    yaml_file = 'HJOPA Flight Scoring Envelope.yml'
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    df = pd.DataFrame(yaml_data)
    markdown_output = "# HJOPA - HondaJet Flight Scoring Envelope\n\n"

    desired_order = ['Evaluate', 'Weight', 'Tolerance Lower', 'Tolerance Upper', 
                     'Tolerance Unit', 'Evaluate lower limit', 'Evaluate upper limit', 'Evaluation Unit']

    for group in df['Group'].unique():
        group_df = df[df['Group'] == group]
        if 'Segment Group' in group_df.columns:
            for segment_group in group_df['Segment Group'].unique():
                segment_group_df = group_df[group_df['Segment Group'] == segment_group]
                markdown_table = create_markdown_table(segment_group_df, desired_order)
                markdown_output += f"## {group}\n### {segment_group}\n\n{markdown_table}\n\n"
        else:
            markdown_table = create_markdown_table(group_df, desired_order)
            markdown_output += f"## {group}\n\n{markdown_table}\n\n"

    # Save the output to a Markdown file
    with open('HJOPA_Flight_Scoring_Envelope.md', 'w') as md_file:
        md_file.write(markdown_output)

if __name__ == "__main__":
    main()
