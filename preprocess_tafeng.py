"""
Preprocessing for tafeng dataset
Will get the same result as previous publications
Weijian Li 
"""
import os
import numpy as np

# transaction_file = 'data/tafeng_data.txt'
transaction_file = 'data/_2_filtered_customer_item_transactions.txt'
customer_freq_dict = dict()
item_freq_dict = dict()
cat_freq_dict = dict()
item_freq_dict_0 = dict()
basket_freq_dict = dict()

with open(transaction_file, 'r') as f:
    for i, each in enumerate(f):
#         if i == 0:
#             continue
        customer_key = each.strip().split(';')[1].strip()
        trans_key = each.strip().split(';')[0].strip().split(' ')[0]
        item_key = each.strip().split(';')[5].strip()
        cat_key = each.strip().split(';')[4].strip()
        try:
            # customer_freq_dict[customer_key].append(trans_key)
            customer_freq_dict[customer_key].append(item_key)
            # customer_freq_dict[customer_key] += 1
        except:
            # customer_freq_dict[customer_key] = [trans_key]
            customer_freq_dict[customer_key] = [item_key]
            # customer_freq_dict[customer_key] = 1          
        try:
            item_freq_dict_0[item_key] += 1
        except:
            item_freq_dict_0[item_key] = 1
        try:
            basket_freq_dict[customer_key].append(trans_key)
        except:
            basket_freq_dict[customer_key] = [trans_key]

# print(customer_freq_dict)
for item, trans_set in basket_freq_dict.items():
    basket_freq_dict[item] = len(set(trans_set))

for item, trans_set in customer_freq_dict.items():
    customer_freq_dict[item] = len(set(trans_set))

customer_key_to_remove = set()
item_key_to_remove_0 = set()

# print(customer_freq_dict)
print(len(customer_freq_dict), len(item_freq_dict_0))
for it, cnt in customer_freq_dict.items():
    if cnt <= 10:
        customer_key_to_remove.add(it)

for it, cnt in basket_freq_dict.items():
    if cnt < 4:
        customer_key_to_remove.add(it)

print(len(customer_key_to_remove))
with open('data/_1_filtered_customer_transactions.txt', 'w') as fw:
    with open(transaction_file, 'r') as f:
        for i, each in enumerate(f):
#             if i == 0:
#                 continue
            customer_key = each.strip().split(';')[1].strip()
            trans_key = each.strip().split(';')[0].strip().split(' ')[0]
            item_key = each.strip().split(';')[5].strip()
            cat_key = each.strip().split(';')[4].strip()
            
            if customer_key in customer_key_to_remove:
                continue
            else:
               fw.write(each)

with open('data/_1_filtered_customer_transactions.txt', 'r') as f:
    for i, each in enumerate(f):
        customer_key = each.strip().split(';')[1].strip()
        trans_key = each.strip().split(';')[0].strip().split(' ')[0]
        item_key = each.strip().split(';')[5].strip()
        cat_key = each.strip().split(';')[4].strip()
        try:
            item_freq_dict[item_key] += 1
        except:
            item_freq_dict[item_key] = 1

item_key_to_remove = set()
for item, count in item_freq_dict.items():
    if count <= 10:
        item_key_to_remove.add(item)

with open('data/_2_filtered_customer_item_transactions.txt', 'w') as fw:
    with open('data/_1_filtered_customer_transactions.txt', 'r') as f:
        for i, each in enumerate(f):
            # if i == 0:
            #     continue
            customer_key = each.strip().split(';')[1].strip()
            trans_key = each.strip().split(';')[0].strip().split(' ')[0]
            item_key = each.strip().split(';')[5].strip()
            cat_key = each.strip().split(';')[4].strip()
            
            if item_key in item_key_to_remove:
                continue
            else:
               fw.write(each)

customer_freq_dict = dict()
item_freq_dict = dict()
cat_freq_dict = dict()

with open('data/_2_filtered_customer_item_transactions.txt', 'r') as f:
    for i, each in enumerate(f):
        # if i == 0:
        #     continue
        customer_key = each.strip().split(';')[1].strip()
        trans_key = each.strip().split(';')[0].strip().split(' ')[0]
        item_key = each.strip().split(';')[5].strip()
        cat_key = each.strip().split(';')[4].strip()
        try:
            customer_freq_dict[customer_key] += 1
        except:
            customer_freq_dict[customer_key] = 1
        try:
            item_freq_dict[item_key] += 1
        except:
            item_freq_dict[item_key] = 1

print(len(customer_freq_dict), len(item_freq_dict))

