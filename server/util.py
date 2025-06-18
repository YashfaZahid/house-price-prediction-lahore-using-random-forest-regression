import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bedroom,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bedroom
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  

    global __model
    if __model is None:
        with open('./artifacts/real_estate_model.pickle', 'rb') as f:
            
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    print("Locations loaded:", __locations) 
    return __locations

def get_data_columns():
    return __data_columns


# def distribute_inheritance(house_price,sons,daughters,brothers,sisters,husband,wives,father,mother):

#     inheritance = {}  

#     father_mother_share = house_price / 6
#     spouse_share=house_price/8
#     total_shares_siblings=(sons*2)+daughters
#     # house_price=(house_price-inheritance["father_share"])-(inheritance["mother_share"])-(inheritance["husband share"])-(inheritance["wife share"])
#     one_share_siblings=house_price/total_shares_siblings


#     if father=="No" and mother=="No" and wives==0 and sons!=0 and daughters!=0:
#         inheritance["sons"]=(one_share_siblings*2)
#         inheritance["daughters"]=(one_share_siblings)

#     elif father=="No" and mother=="No" and wives!=0 and sons==0 and daughters==0:
#         inheritance["wife share"]=house_price*(1/4)

#     elif father=="No" and mother=="No" and wives!=0 and sons!=0 and daughters!=0:
#         inheritance["wife share"]=spouse_share/wives
#         house_price=(house_price-(inheritance["wife share"]))
#         one_share_siblings=house_price/total_shares_siblings
#         inheritance["sons"]=(one_share_siblings*2)
#         inheritance["daughters"]=(one_share_siblings)

#     elif father=="Yes" and mother=="Yes" and wives!=0 and sons!=0 and daughters!=0:
#         inheritance["father_share"] = father_mother_share
#         inheritance["mother_share"] = father_mother_share
#         inheritance["wife share"]=spouse_share
#         house_price=house_price=(house_price-(inheritance["wife share"])-(inheritance["father_share"])-(inheritance["mother_share"]))
#         one_share_siblings=house_price/total_shares_siblings
#         inheritance["sons"]=(one_share_siblings*2)
#         inheritance["daughters"]=(one_share_siblings)

#     elif father=="No" and mother=="No" and wives==0 and sons==0 and daughters==1:
#         inheritance["daughters"]=house_price/2

#     elif father=="No" and mother=="No" and wives==0 and sons==1 and daughters==0:
#         inheritance["sons"]=house_price

#     elif father=="Yes" and mother=="Yes" and wives!=0 and sons==0 and daughters==1:
#         inheritance["father_share"] = father_mother_share
#         inheritance["mother_share"] = father_mother_share
#         inheritance["wife share"]=spouse_share
#         house_price=house_price=(house_price-(inheritance["wife share"])-(inheritance["father_share"])-(inheritance["mother_share"]))
#         one_share_siblings=house_price/total_shares_siblings
#         inheritance["daughters"]=house_price/2

#     elif father=="Yes" and mother=="Yes" and wives==0 and sons==0 and daughters==1:
#     # # parents
#     # if father == "Yes" and mother == "Yes":
#     #     inheritance["father_share"] = father_mother_share
#     #     inheritance["mother_share"] = father_mother_share
#     # elif father == "Yes":
#     #     inheritance["father_share"] = father_mother_share
#     #     inheritance["mother_share"] = 0
#     # elif mother == "Yes":
#     #     inheritance["mother_share"] = father_mother_share
#     #     inheritance["father_share"] = 0
#     # else:
#     #     inheritance["father_share"] = 0
#     #     inheritance["mother_share"] = 0

#     # # spouse
#     # if  wives!=0 and husband =="No":
#     #     inheritance["wife share"]=spouse_share/wives
#     #     inheritance["husband share"]=0
#     # elif husband=="Yes":
#     #     inheritance["wife share"]=0
#     #     inheritance["husband share"]=spouse_share
#     # else:
#     #     inheritance["wife share"]=0
#     #     inheritance["husband share"]=0 


#     # # Children 
#     # house_price=(house_price-inheritance["father_share"])-(inheritance["mother_share"])-(inheritance["husband share"])-(inheritance["wife share"])
#     # one_share_siblings=house_price/total_shares_siblings

#     # if sons!=0 and daughters!=0:
#     #     inheritance["sons"]=(one_share_siblings*2)*sons
#     #     inheritance["daughters"]=(one_share_siblings)*daughters
#     # elif sons==0 and daughters==1:
#     #     inheritance["daughters"]=house_price/2
#     #     inheritance["sons"]=0
#     #     inheritance["father_share"]=house_price/2
#     # elif sons==0 and daughters>1:
#     #     inheritance["daughters"]=house_price*(2/3)
#     #     inheritance["sons"]=0
#     #     inheritance["father_share"]=house_price/2
#     # elif daughters==0:
#     #     inheritance["sons"]=(one_share_siblings*2)*sons
#     #     inheritance["daughters"]=0
#     # else:
#     #     inheritance["sons"]=0
#     #     inheritance["daughters"]=0





if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("bahria town, lahore, punjab",2500,4,4))