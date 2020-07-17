import click
import pandas as pd

def read_csv(file):
    return pd.read_csv(file)

def process_csv(df):
    df.append(df.tail())
    #do some stuff, filler
    return df

def write_excel(df, file):
    df.to_excel(file)

@click.command()
@click.option("--in", "-i", "in_file", required=True, 
    help="Path to csv file to be processed", 
    type=click.Path(exists=True, dir_okay=False, readable=True))
@click.option("--out", "-o", "out_file", default="./output.xlsx", 
    help="Path to excel file to store result.", 
    type=click.Path(dir_okay=False))

def process(in_file, out_file):
    """Processes the input file IN and stores the result to output file OUT."""
    input = read_csv(in_file)
    output = process_csv(input)
    write_excel(output, out_file)

if __name__ == "__main__":
    process()