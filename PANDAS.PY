import pandas as pd

a={
    "Name":["azaan","hasan","jibran",None,"iftikar","ali",None,"hussain","asghar","mujahid","subtain","zulqarnian","azaan"],
    "Age":[12,23,34,45,56,None,34,5,65,"asd",89,23,12],
    "City":["islamabad","lahore",None,"karachi","islamabad","multan","surgoda",None,"hasanabdal","munsehrra","multan","sargoda","islamabad"],
    "Marks":[234,455,455,245,567,232,454,453,123,334,456,134,234]

}
b=pd.DataFrame(a,index=[0,1,2,3,4,5,6,7,8,9,10,11,12])
print(b)

#   column add

b["Salary"]=[1200,1300,1400,1100,1500,1200,2300,340,450,560,230,120,230]
print(b)

# column name chnge

b.rename(columns={"Salary":"Monthly_Salary"},inplace=True)
print(b)


# some basic information about dataset 

print(b.shape)
print(b.columns)
print(b.dtypes)
print(b.describe())
print(b.info())


# check kro ke koe dataset kahli na ho
print(b.isnull())                                   # true / false dega agr true hoya tu missing ai 
print(b.isnull().sum())                             # hr column ki entries bthiye ga ke ketni missing hai 
print(b.isnull().sum().sum())                       # yah pr apko number bata dega ke ketne entries missing hai 

# row remove agr koe name nhi hai tu 

b=b.dropna(subset=["Name"])
print(b)
print(len(b))

# agr index 0,1,2,3 starting se aisi hi chiye tu 

b=b.dropna(subset=["Name"]).reset_index(drop=True)
print(b)


# agr kese integar me string value galti se ajiye tu 

b["Age"]=pd.to_numeric(b["Age"],errors="coerce")
print(b)

# ab missing value ya drop krte hain ya fill krte hain 2 hi option hote hain 

b["Age"]=b["Age"].fillna(b["Age"].median())
print(b)

b["City"]=b["City"].fillna("unknwon")
print(b)


# agr kese column ke andr spelling mistake hon aur wo teakh krne ho tu 

b["City"]=b["City"].replace({
    "surgoda":"sarghoda",
    "munsehrra":"Munsehra"
})
print(b)


# check kro ke ab agr validation lagani hai tu 

print(b[b["Age"]<20])

b.loc[b["Age"]<20,"Age"]=None
print(b)


# agr apko koe function apply krna hai kese pr tu 

def age_group(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

b["Age_Group"] = b["Age"].apply(age_group)

# check kro ab dataset ketne rows duplicate hain 

print(b.duplicated())
print(b.duplicated().sum())
b=b.drop_duplicates(subset=["Name"])
print(b)




#                       #                       project 2               #                           #

import pandas as pd

a={
    "Transaction_ID": ["TXN-1001", "TXN-1002", "TXN-1003", "TXN-1001", "TXN-1005", "TXN-1006", "TXN-1007", "TXN-1008", "TXN-1009", "TXN-1010"],
    "Customer_Name": ["Ali Khan", "  sara ahmed ", "Ayesha", "Ali Khan", "John Doe", None, "Fatima", "Ali", "Zainab", "  sara ahmed "],
    "Age": [25, 30, "twenty-two", 25, 45, 29, None, 35, 150, 30], # Note the string "twenty-two" and outlier 150
    "City": ["Lahore", "karachi", "ISLAMABAD", "Lahore", "Lahore", "Faisalabad", None, "Lahore ", "multan", "karachi"], # Note casing & trailing spaces
    "Purchase_Amount": ["$1,200.50", "450.00", "NaN", "$1,200.50", "890", "unknown", "340.20", "$560", "1200.00", "450.00"], # Note currency signs and strings
    "Rating": [4.5, 3.0, 5.0, 4.5, 2.1, 4.0, None, 1.5, 3.5, 3.0],
    "Signup_Date": ["2025-01-12", "15/01/2025", "2025-01-10", "2025-01-12", "01-20-2025", "2025-01-18", None, "2025-01-22", "2025-01-25", "15/01/2025"] # Note mixed date formats
}
b=pd.DataFrame(a)
print(b)

print(b.shape)
print(b.columns)
print(b.dtypes)
print(b.info())
print(b.describe())
print(len(b))

print(b.isnull())
print(b.isnull().sum())
print(b.isnull().sum().sum())

b=b.dropna(subset=["Customer_Name"]).reset_index(drop=True)
print(b)

b["Age"]=pd.to_numeric(b["Age"],errors="coerce")
print(b)

b["Age"]=b["Age"].fillna(b["Age"].mean())
print(b)

b["City"]=b["City"].fillna("unknown")
print(b)

print(b.duplicated())
b=b.drop_duplicates(subset=["Transaction_ID"])
print(b)

b=b.reset_index(drop=True)
print(b)

print("\n================================================")

b["Rating"]=b["Rating"].fillna(b["Rating"].mean())
print(b)

b["Purchase_Amount"] = pd.to_numeric( b["Purchase_Amount"],errors="coerce")
b["Purchase_Amount"] = b["Purchase_Amount"].fillna(b["Purchase_Amount"].mean())
print(b)


b["Signup_Date"] = pd.to_datetime(b["Signup_Date"],errors="coerce",format="mixed")
b["Signup_Date"]=b["Signup_Date"].fillna(b["Signup_Date"].mode()[0])
print(b)

b["City"] = b["City"].str.title()
b["City"]=b["City"].str.strip()
print("\n=====================================")
b["City"]=b["City"].fillna("unknown")
print(b)

b.loc[b["Customer_Name"] == "Ali Khan", "Customer_Name"] = "azaan"
print(b)
b.loc[b["Customer_Name"]=="Fatima","Customer_Name"]="zahra"
print(b)

# b.loc[10,"customer_name"]="bahadar"           # ais trh bi kr skhte ho 
# print(b)