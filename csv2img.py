import numpy as np
import pandas as pd
import os.path
import argparse
from PIL import Image

def import_from_csv(csv_path):

    df = pd.read_csv(csv_path)
    df = df.drop('src_ip',1)
    df.columns = df.columns.str.replace('payload_bit_', '')
    df = df.replace(-1, 0)

    return df

def bit_to_byte(df):

    df2 = pd.DataFrame()

    i = 0
    j = 0
    while i < len(df.columns):
        df2[j] = df[str(i+7)] + 2*df[str(i+6)] + 4*df[str(i+5)] + 8*df[str(i+4)] + 16*df[str(i+3)] + 32*df[str(i+2)] + 64*df[str(i+1)] + 128*df[str(i)]
        i = i+8
        j = j+1

    return df2

def build_img(df2, output_path, index_offset):

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print("Directory ", output_path, " Created")
    else:
        print("Directory ", output_path, " already exists")
        
    for i in range(0,len(df2.index)):
        j = 0
        df5 = pd.DataFrame()
        
        while j < len(df2.columns):
            df4 = df2.iloc[i:i+1, j:j+32]
        
            if j == 0:
                array4 = df4.to_numpy()
        
            else:
                array5 = df4.to_numpy()
                array4 = np.append(array4, array5, axis=0)
        
            j = j+32
        
        img4 = Image.fromarray(np.uint8(array4))
        img_path = output_path+str(i+index_offset)+'.png'
        img4.save(img_path, 'PNG')
        print("Created ", img_path)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--r', type=str, required=True)
    parser.add_argument('--w', type=str, required=True)
    parser.add_argument('--i', type=int, required=True)
    args = parser.parse_args()

    csv_path = args.r
    output_path = args.w
    index_offset = args.i

    df = import_from_csv(csv_path)
    df = bit_to_byte(df)
    build_img(df, output_path, index_offset)

if __name__ == '__main__':
    main()
