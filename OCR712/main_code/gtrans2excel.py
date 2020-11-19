import io, os
from google.cloud import vision_v1
import pandas as pd
import openpyxl
  
column_names = ["अहवाल दिनांक", "जिल्हा", "गाव", "गट क्रमांक व उपविभाग", "तालुका", "Crops Grown"]

df = pd.DataFrame(columns = column_names)

def txt2df():
    date=""
    jilha=""
    gav=""
    gutKrmank=""
    taluka=""
    cropsGrown=[]
    # print(df)
    flag =0

    with open ('message.txt', 'rt', encoding="utf8") as myfile:  # Open lorem.txt for reading
        for myline in myfile:              # For each line, read to a string,
            # print(myline)                  # and print the string.
            if flag == 1:
                cropsGrown.append(myline.replace(" ","").replace("\n",""))
                print("added crop")
                flag = 0
            if "अहवाल दिनांक" in myline and date=="":
                print("FOUND date")
                try:
                    temp= myline.split(":",1)[1].replace(" ","")
                    date=(temp)
                    print(temp)
                except Exception as e:
                    print("dinank ",e)
                
                
                # df= df.append({"अहवाल दिनांक":temp})
                # print(df)
            elif "जिल्हा" in myline and jilha=="":
                print("FOUND jilha")
                try:
                    temp= myline.split(":-",1)[1].replace(" ","")
                    print(temp)
                    jilha=(temp)
                except Exception as e:
                    print("jilha ",e)
                
            elif "गाव :" in myline and gav=="":
                print("FOUND gav")
                try:
                    temp= myline.split(":-",1)[1].replace(" ","")
                    print(temp)
                    gav=(temp)
                except Exception as e:
                    print("gav ",e)
                
            elif "क्रमांक व उपविभाग :" in myline and gutKrmank=="":
                print("FOUND gutKrmank")
                try:
                    temp= myline.split(":",1)[1].replace(" ","")
                    print(temp)
                    gutKrmank=(temp)
                except Exception as e:
                    print("kramank ",e)
            elif "तालुका" in myline and taluka=="":
                print("FOUND taluka")
                try:
                    temp= myline.split(":-",1)[1].replace(" ","")
                    print(temp)
                    taluka=(temp)
                except Exception as e:
                    print("taluka ",e)
                
            elif ("2017" in myline) or ("2018" in myline) or ("2019" in myline)or ("2020" in myline)or ("2016" in myline)or ("2015" in myline)or ("2014" in myline)or ("2013" in myline)or ("2012" in myline)or ("2011" in myline):
            #or "2013" or "2014" or "2015" or "2016" or "2017" or "2018" or "2019" or "2020" :
                print("found crop")
                flag = 1
    print("crops: -", cropsGrown)
    CROPS= ', '.join(map(str, cropsGrown))
    print("STRING CROPS ",CROPS)
    df.loc[len(df.index)] = [date,jilha,gav,gutKrmank,taluka,CROPS]

# print(df)

# df.to_csv("output.csv")
# df.to_excel("output1432432.xlsx") 




ch = ""
def sample_batch_annotate_files(file_path="input2.pdf"):
    """Perform batch file annotation."""
    client = vision_v1.ImageAnnotatorClient()

    # Supported mime_type: application/pdf, image/tiff, image/gif
    mime_type = "application/pdf"
    with io.open(file_path, "rb") as f:
        content = f.read()
    input_config = {"mime_type": mime_type, "content": content}
    features = [{"type_": vision_v1.Feature.Type.DOCUMENT_TEXT_DETECTION}]

    # The service can process up to 5 pages per document file. Here we specify
    # the first, second, and last page of the document to be processed.
    pages = [1, 2, -1]
    requests = [{"input_config": input_config, "features": features, "pages": pages}]

    response = client.batch_annotate_files(requests=requests)
    file1 = open("message.txt", "w")  # write mode 
    file1.write("") 
    file1.close() 
    for image_response in response.responses[0].responses:
        print(u"Full text:\n{}".format(image_response.full_text_annotation.text))
        file1 = open("message.txt", "a", encoding="utf8")  # append mode 
        file1.write(image_response.full_text_annotation.text) 
        file1.close() 

# while ch != "2":
#     ch=input(" 1 for new pdf, 2 for end ")
#     if(ch == "1"):
#         filename=input("enter pdf loc ")
#         try:
#             sample_batch_annotate_files(filename)
#             txt2df()
#         except:
#             print("path error")
#     elif(ch == "2"):
#         print(df)
#         try:
#             df.to_excel("output69.xlsx") 
#             print("your excel is ready")
#         except:
#             print("close excel then rerun")
#     else:
#         print("invalid i/p")

# import wget

def test():
    filesPath = "D:\\TP_PROGS\\Projects\\CodeForChangeHackathon2020\\progs\\OCRCFC2020\\media\\documents"
    # BASE_DIR = os.path.join( os.path.dirname( filesPath ), '..' )
    # BASE_DIR2 = os.path.join( os.path.dirname( BASE_DIR ), '..' )
    # print(BASE_DIR)
    print("DIRECTOEYYYYYYyyyyyyyyyyyyyyyyyyyyyy",os.listdir(filesPath))
    fileNames=os.listdir(filesPath)
    for file in fileNames:
        temp = "D:\\TP_PROGS\\Projects\\CodeForChangeHackathon2020\\progs\\OCRCFC2020\\media\\documents\\"+file
        try:
            sample_batch_annotate_files(temp)
            txt2df()
        except Exception as e:
            print("path error ",e)
    print(df)
    try:
        os.remove("D:\\TP_PROGS\\Projects\\CodeForChangeHackathon2020\\progs\\OCRCFC2020\\output.xlsx")
        print("EXCEL REMOVEDDDDD")
    except:
        print("no file to remove")
    try:
        df.to_excel("output.xlsx") 
        print("your excel is ready!!!!!!")
        df.drop(df.index, inplace=True)
    except:
        print("close excel then rerun")
    
    

    # print('Beginning file download with wget module')

    # url = 'D:\\TP_PROGS\\Projects\\CodeForChangeHackathon2020\\progs\\OCRCFC2020\\output.xlsx'
    # wget.download(url, 'C:\\')





            


