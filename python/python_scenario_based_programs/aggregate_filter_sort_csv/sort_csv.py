# big
import pandas as pd
import os
import time
import shutil
import uuid
import traceback

def parse_type(s):
    if s.isdigit():
        return int(s)
    try:
        res = float(s)
        return res
    except:
        return s

def pos_by(by,head,sep):
    by_num = 0
    for col in head.split(sep):
        if col.strip()==by:
            break
        else:
            by_num+=1
    return by_num

def merge_sort(directory,ofile,by,ascending=True,sep=","):
    with open(ofile,"w") as outfile:  # full outfile
        file_list = os.listdir(directory)  # list of chunked sorted files
        file_chunk = [open(directory+"/"+file,"r") for file in file_list]  # list of opened chunked sorted files
        k_row = [file_chunk[i].readline()for i in range(len(file_chunk))]  # list of header row of each sorted chunk
        by = pos_by(by,k_row[0],sep)  # position of needed column from header of first sorted chunk
        outfile.write(k_row[0])  # write header to full out file
        k_row = [file_chunk[i].readline()for i in range(len(file_chunk))]  # list of first line of each sorted chunk
        print(k_row)
        k_by = [parse_type(k_row[i].split(sep)[by].strip()) for i in range(len(file_chunk))]  # required value from 1st line of each chunk
    with open(ofile,"a") as outfile:
        while True:
            for i in range(len(k_by)):
                if i >= len(k_by):
                    break
                sorted_k_by = sorted(k_by) if ascending else sorted(k_by,reverse=True)  # sort first line from each chunk
                if k_by[i] == sorted_k_by[0]:
                    print(f"writing {k_row[i]}")
                    outfile.write(k_row[i])
                    k_row[i] = file_chunk[i].readline()
                    print(k_row)
                    if not k_row[i]:
                        file_chunk[i].close()
                        del(file_chunk[i])
                        del(k_row[i])
                        del(k_by[i])
                    else:
                        k_by[i] = parse_type(k_row[i].split(sep)[by].strip())
            if len(k_by)==0:
                break

def external_sort(file_path,by,ofile,tmp_dir,ascending=True,chunksize=3,sep=",", usecols=None,index_col=None):
    os.makedirs(tmp_dir,exist_ok=True)  # tmp dir for intermediate files
    try:
        data_chunk = pd.read_csv(file_path,sep=sep,usecols=usecols,index_col=index_col,chunksize=chunksize)  # chunked full file
        for chunk_number, chunk in enumerate(data_chunk):  # for each chunk in full file
            chunk = chunk.sort_values(by,ascending=ascending)  # sort chunk from full file
            chunk.to_csv(tmp_dir+"/"+str(chunk_number)+".csv",index=None,sep=sep)  # sorted chunk file from full file
        merge_sort(tmp_dir,ofile=ofile,by=by,ascending=ascending,sep=sep)  # merge sort all sorted chunks of full file
    except Exception:
        print(traceback.format_exc())
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

if __name__ == "__main__":
    infile = "C:\REPOSITORIES\MyRepo\python\python_file_handling\sample_data.csv"  # full input file
    ofile = "C:\REPOSITORIES\MyRepo\python\python_file_handling\sample_data_sorted.csv"  # full output file
    tmp = "C:\REPOSITORIES\MyRepo\python\python_file_handling/tmp"  # tmp dir for intermediate files
    external_sort(infile,"amount",ofile,tmp,ascending=True,chunksize=3,sep=",")  # full sort