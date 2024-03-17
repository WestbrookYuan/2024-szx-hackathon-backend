import random



# products = {
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e": {
#     "brand": "Apple",
#     "description": "iPhone Pro Max Units"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d4": {
#     "brand": "Nike",
#     "description": "Shoeboxes of Air Jordan Sneakers"
#   },
#   "http://localhost:8080/logistics-objects/dfd3f904-fd4c-4120-8775-b110032419a8": {
#     "brand": "Coca-Cola",
#     "description": "Bottled Soft Drinks in Bulk Cases"
#   },
#   "http://localhost:8080/logistics-objects/65a04936-ff08-4f60-bb6c-23644b124ef3": {
#     "brand": "Louis Vuitton",
#     "description": "Leather Handbags in Master Cartons"
#   },
#   "http://localhost:8080/logistics-objects/2226d445-e1cc-4600-94c5-49ec57520f83": {
#     "brand": "Toyota",
#     "description": "Automotive Spare Parts Containers"
#   },
#   "http://localhost:8080/logistics-objects/d75fe5ee-c8b2-4a4f-a640-85d27c2c2bf6": {
#     "brand": "Mercedes-Benz",
#     "description": "A-Class Sedan Auto Parts Shipment"
#   },
#   "http://localhost:8080/logistics-objects/8fbad5f9-0cf5-4d3c-b1b2-1055e91a93fa": {
#     "brand": "Samsung",
#     "description": "Galaxy Smartphone Inventory Lot"
#   },
#   "http://localhost:8080/logistics-objects/4d8893ac-9919-474a-9bad-f04a195adaa8": {
#     "brand": "McDonald's",
#     "description": "Frozen Food and Packaging Supplies"
#   },
#   "http://localhost:8080/logistics-objects/775efaa6-ecf3-4344-bf7e-94b564e8fdd5": {
#     "brand": "Amazon",
#     "description": "Kindle E-Readers and Echo Devices Cargo"
#   },
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e0": {
#     "brand": "Microsoft",
#     "description": "Xbox Consoles and Surface Tablets Shipment"
#   },
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e1": {
#     "brand": "Gucci",
#     "description": "Designer Clothing and Accessories Parcel"
#   },
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e2": {
#     "brand": "Adidas",
#     "description": "Performance Sportswear and Shoes Crate"
#   },
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e3": {
#     "brand": "Pepsi",
#     "description": "Cola Beverages in Industrial Quantities"
#   },
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e4": {
#     "brand": "BMW",
#     "description": "Car Components and Accessories Freight"
#   },
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e5": {
#     "brand": "Huawei",
#     "description": "Mate Series Smartphones and Laptops Pallet"
#   },
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e6": {
#     "brand": "Chanel",
#     "description": "Perfumes, Cosmetics and Fashion Goods Bundle"
#   },
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e7": {
#     "brand": "Unilever",
#     "description": "Consumer Products and Personal Care Goods Load"
#   },
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e8": {
#     "brand": "Procter & Gamble",
#     "description": "Household and Personal Care Product Cargo"
#   },
#   "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e9": {
#     "brand": "Disney",
#     "description": "Licensed Merchandise and Toys Container"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d40": {
#     "brand": "Tesla",
#     "description": "Electric Vehicle Components and Batteries Shipment"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d41": {
#     "brand": "Sony",
#     "description": "PlayStation Consoles and Bravia TVs Box"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d42": {
#     "brand": "Starbucks",
#     "description": "Coffee Beans and Retail Store Supplies Package"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d43": {
#     "brand": "Intel",
#     "description": "Computer Processors and Chips Consignment"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d44": {
#     "brand": "Estée Lauder",
#     "description": "Skincare and Makeup Products Batch"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d45": {
#     "brand": "L'Oreal",
#     "description": "Cosmetics and Haircare Products Shipment"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d46": {
#     "brand": "IKEA",
#     "description": "Flat-Packed Furniture and Home Decor Items Crate"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d47": {
#     "brand": "Zara",
#     "description": "Fast-Fashion Garments and Accessories Bundle"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d48": {
#     "brand": "Volkswagen",
#     "description": "Auto Parts and Components Transport"
#   },
#   "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d49": {
#     "brand": "Lenovo",
#     "description": "ThinkPad Laptops and Desktop Computers Shipment"
#   },
#   "http://localhost:8080/logistics-objects/dfd3f904-fd4c-4120-8775-b110032419a80": {
#     "brand": "Nestle",
#     "description": "Food and Beverage Products in Bulk Quantity"
#   }
# }


# for item in products:
#   product = products[item]
#   print("\n----------------------")
#   print(item)
#   s = '''
#   \n
#     {
#       "@context": {
#         "cargo": "https://onerecord.iata.org/ns/cargo#"
#       },
#       "@type": "cargo:Product",
#       "cargo:description": "%s",
#       "cargo:hsCode": "123456",
#       "cargo:uniqueIdentifier": "A2650",
#       "cargo:manufacturer": {
#         "@type": "cargo:Company",
#         "cargo:name": "%s"
#       }
#     }
#   ''' % (product["description"], product["brand"])
#   print(s)



# sphs = [
#   {'@type': 'cargo:HandlingInstructions', 'cargo:serviceType': 'SPH', 'cargo:serviceDescription': 'Valuable Cargo', 'cargo:serviceTypeCode': 'VAL'}, 
#   {'@type': 'cargo:HandlingInstructions', 'cargo:serviceType': 'SPH', 'cargo:serviceDescription': 'highest priority', 'cargo:serviceTypeCode': 'AAA'}, 
#   {'@type': 'cargo:HandlingInstructions', 'cargo:serviceType': 'SPH', 'cargo:serviceDescription': 'living animal', 'cargo:serviceTypeCode': 'AVI'}, 
#   {'@type': 'cargo:HandlingInstructions', 'cargo:serviceType': 'SPH', 'cargo:serviceDescription': 'covid vaccine', 'cargo:serviceTypeCode': 'CCV'}, 
#   {'@type': 'cargo:HandlingInstructions', 'cargo:serviceType': 'SPH', 'cargo:serviceDescription': 'perishable goods', 'cargo:serviceTypeCode': 'PER'}
# ]

# pieces = {
#   "piece1": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0d93bdfe-cfbb-4062-867c-77799c637c3e","http://localhost:8080/logistics-objects/5ea24251-b69b-4f25-a12b-4e1578dec5f2","http://localhost:8080/logistics-objects/5844181f-e932-4133-a250-a849771ade6a",
#       "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d4", 
#       "http://localhost:8080/logistics-objects/2226d445-e1cc-4600-94c5-49ec57520f83"
#       ],
#     "grossWeight": "800",
#     "id": "http://localhost:8080/logistics-objects/103cf0fb-868e-41d0-96ce-d601b10de136" 
#   },
#   "piece2": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0600023b-c822-4ee4-a89e-a30030fa7535","http://localhost:8080/logistics-objects/0d93bdfe-cfbb-4062-867c-77799c637c3e","http://localhost:8080/logistics-objects/e903654e-0015-476f-88fc-75613e11bd8e","http://localhost:8080/logistics-objects/0ea48b9a-c152-47cc-a370-353c57535c79","http://localhost:8080/logistics-objects/d4bf4fe9-f512-4f7e-a992-c7f5dab98373",
#       "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e3",
#       "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d47"
#       ],
#     "grossWeight": "1200",
#     "id": "http://localhost:8080/logistics-objects/d67da3bf-d718-4306-b5f1-e1f11a77a4cb" 
#   },
#   "piece3": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0d93bdfe-cfbb-4062-867c-77799c637c3e","http://localhost:8080/logistics-objects/880af942-d48f-4b6a-a8c7-9a7a55c6375d","http://localhost:8080/logistics-objects/e903654e-0015-476f-88fc-75613e11bd8e","http://localhost:8080/logistics-objects/0f19246a-929e-4605-88c7-2b1720f2dd83","http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e4", "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e9"],
#     "grossWeight": "1100",
#     "id": "http://localhost:8080/logistics-objects/745fdfc8-d8b5-42c1-802d-b28fb9aff8d6" 
#   },
#   "piece4": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0600023b-c822-4ee4-a89e-a30030fa7535","http://localhost:8080/logistics-objects/880af942-d48f-4b6a-a8c7-9a7a55c6375d","http://localhost:8080/logistics-objects/e903654e-0015-476f-88fc-75613e11bd8e","http://localhost:8080/logistics-objects/29f41c6d-2d4a-4566-8a64-bc1a45e0af85","http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d46", "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d40"],
#     "grossWeight": "1500",
#     "id": "http://localhost:8080/logistics-objects/83ed91ee-2b6d-40eb-80c2-4824007965e1" 
#   },
#   "piece5": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0d93bdfe-cfbb-4062-867c-77799c637c3e","http://localhost:8080/logistics-objects/5ea24251-b69b-4f25-a12b-4e1578dec5f2","http://localhost:8080/logistics-objects/d4bf4fe9-f512-4f7e-a992-c7f5dab98373","http://localhost:8080/logistics-objects/bfd7b0d1-98b2-41cb-a378-1a6d707c625a","http://localhost:8080/logistics-objects/4cd33837-e25f-49af-a1ed-8d010648b0aa","http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d42", "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e0"],
#     "grossWeight": "900",
#     "id": "http://localhost:8080/logistics-objects/a4e2b28f-e47d-45b9-85c5-90605e3e3107" 
#   },
#   "piece6": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0d93bdfe-cfbb-4062-867c-77799c637c3e","http://localhost:8080/logistics-objects/d4bf4fe9-f512-4f7e-a992-c7f5dab98373","http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e5", "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d49"],
#     "grossWeight": "1300",
#     "id": "http://localhost:8080/logistics-objects/aa8d9022-e962-4ca0-b948-861cde36caa6" 
#   },
#   "piece7": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/f8de44f3-f700-4878-889c-f22ee676e1e4","http://localhost:8080/logistics-objects/5ea24251-b69b-4f25-a12b-4e1578dec5f2","http://localhost:8080/logistics-objects/0ea48b9a-c152-47cc-a370-353c57535c79","http://localhost:8080/logistics-objects/0f19246a-929e-4605-88c7-2b1720f2dd83","http://localhost:8080/logistics-objects/29f41c6d-2d4a-4566-8a64-bc1a45e0af85","http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e7", "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d41"],
#     "grossWeight": "1000",
#     "id": "http://localhost:8080/logistics-objects/5ce75683-415a-4177-bc18-bd358a56b124" 
#   },
#   "piece8": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0600023b-c822-4ee4-a89e-a30030fa7535","http://localhost:8080/logistics-objects/832e85f2-3701-44fa-8c04-22f279f385c1","http://localhost:8080/logistics-objects/5ea24251-b69b-4f25-a12b-4e1578dec5f2","http://localhost:8080/logistics-objects/4cd33837-e25f-49af-a1ed-8d010648b0aa","http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d44", "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e2"],
#     "grossWeight": "1150",
#     "id": "http://localhost:8080/logistics-objects/1ed09d5e-aece-457f-ab4c-6ac5abc95c2d" 
#   },
#   "piece9": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0d93bdfe-cfbb-4062-867c-77799c637c3e","http://localhost:8080/logistics-objects/832e85f2-3701-44fa-8c04-22f279f385c1","http://localhost:8080/logistics-objects/5ea24251-b69b-4f25-a12b-4e1578dec5f2","http://localhost:8080/logistics-objects/b9f4889f-fc13-4375-97fa-2b25b3e2d575","http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d48", "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e8"],
#     "grossWeight": "1406",
#     "id": "http://localhost:8080/logistics-objects/d6393bee-38e0-4c42-923e-a5cb0eaa1d2f" 
#   },
#   "piece10": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/68ae5378-a153-431e-995b-3c1b8b35ca8a","http://localhost:8080/logistics-objects/e903654e-0015-476f-88fc-75613e11bd8e","http://localhost:8080/logistics-objects/a629fbb3-9b4c-46b1-8332-c33166bd1085","http://localhost:8080/logistics-objects/5844181f-e932-4133-a250-a849771ade6a","http://localhost:8080/logistics-objects/0f19246a-929e-4605-88c7-2b1720f2dd83","http://localhost:8080/logistics-objects/dfd3f904-fd4c-4120-8775-b110032419a8", "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e6"],
#     "grossWeight": "1053",
#     "id": "http://localhost:8080/logistics-objects/559bdc8e-c635-4391-b7f3-8f5bfa0e183b" 
#   },
#   "piece11": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/68ae5378-a153-431e-995b-3c1b8b35ca8a","http://localhost:8080/logistics-objects/e903654e-0015-476f-88fc-75613e11bd8e","http://localhost:8080/logistics-objects/d4bf4fe9-f512-4f7e-a992-c7f5dab98373","http://localhost:8080/logistics-objects/29f41c6d-2d4a-4566-8a64-bc1a45e0af85","http://localhost:8080/logistics-objects/1bdd35b5-d51d-4460-ae0d-4644d7794c49","http://localhost:8080/logistics-objects/65a04936-ff08-4f60-bb6c-23644b124ef3", "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d45"],
#     "grossWeight": "1250",
#     "id": "http://localhost:8080/logistics-objects/98ed5abf-6317-43b9-adce-4e69734584f1" 
#   },
#   "piece12": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0600023b-c822-4ee4-a89e-a30030fa7535","http://localhost:8080/logistics-objects/68ae5378-a153-431e-995b-3c1b8b35ca8a","http://localhost:8080/logistics-objects/f8de44f3-f700-4878-889c-f22ee676e1e4","http://localhost:8080/logistics-objects/1bdd35b5-d51d-4460-ae0d-4644d7794c49","http://localhost:8080/logistics-objects/b9f4889f-fc13-4375-97fa-2b25b3e2d575","http://localhost:8080/logistics-objects/0ea48b9a-c152-47cc-a370-353c57535c79","http://localhost:8080/logistics-objects/a629fbb3-9b4c-46b1-8332-c33166bd1085","http://localhost:8080/logistics-objects/8fbad5f9-0cf5-4d3c-b1b2-1055e91a93fa", "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d43"],
#     "grossWeight": "950",
#     "id": "http://localhost:8080/logistics-objects/c841a3af-74b6-4c20-a733-bcd7970d872d" 
#   },
#   "piece13": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0c931213-7fc3-4264-8a01-da0ab1a2711c","http://localhost:8080/logistics-objects/e1f8e40c-dd8d-43ec-ae10-2863f04ac2c1","http://localhost:8080/logistics-objects/0600023b-c822-4ee4-a89e-a30030fa7535","http://localhost:8080/logistics-objects/0f19246a-929e-4605-88c7-2b1720f2dd83","http://localhost:8080/logistics-objects/bfd7b0d1-98b2-41cb-a378-1a6d707c625a","http://localhost:8080/logistics-objects/68ae5378-a153-431e-995b-3c1b8b35ca8a","http://localhost:8080/logistics-objects/d75fe5ee-c8b2-4a4f-a640-85d27c2c2bf6", "http://localhost:8080/logistics-objects/dfd3f904-fd4c-4120-8775-b110032419a80"],
#     "grossWeight": "1352",
#     "id": "http://localhost:8080/logistics-objects/7d13e2ab-7489-43cd-bf7f-af6f8b94d8fe" 
#   },
#   "piece14": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/68ae5378-a153-431e-995b-3c1b8b35ca8a","http://localhost:8080/logistics-objects/d9abe475-9844-4599-af49-b162cec4c14d","http://localhost:8080/logistics-objects/a629fbb3-9b4c-46b1-8332-c33166bd1085","http://localhost:8080/logistics-objects/775efaa6-ecf3-4344-bf7e-94b564e8fdd5", "http://localhost:8080/logistics-objects/4d8893ac-9919-474a-9bad-f04a195adaa8"],
#     "grossWeight": "1000",
#     "id": "http://localhost:8080/logistics-objects/51c37027-e11c-4777-8ba7-bd6fc3e33102" 
#   },
#   "piece15": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0c931213-7fc3-4264-8a01-da0ab1a2711c","http://localhost:8080/logistics-objects/d9abe475-9844-4599-af49-b162cec4c14d","http://localhost:8080/logistics-objects/880af942-d48f-4b6a-a8c7-9a7a55c6375d","http://localhost:8080/logistics-objects/a629fbb3-9b4c-46b1-8332-c33166bd1085","http://localhost:8080/logistics-objects/832e85f2-3701-44fa-8c04-22f279f385c1","http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e1", "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d47"],
#     "grossWeight": "119",
#     "id": "http://localhost:8080/logistics-objects/776b8599-530e-4b3b-a2e9-b12bbc246a75" 
#   },
#   "piece16": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/e1f8e40c-dd8d-43ec-ae10-2863f04ac2c1","http://localhost:8080/logistics-objects/d9abe475-9844-4599-af49-b162cec4c14d","http://localhost:8080/logistics-objects/0ea48b9a-c152-47cc-a370-353c57535c79","http://localhost:8080/logistics-objects/29f41c6d-2d4a-4566-8a64-bc1a45e0af85","http://localhost:8080/logistics-objects/b9f4889f-fc13-4375-97fa-2b25b3e2d575","http://localhost:8080/logistics-objects/4cd33837-e25f-49af-a1ed-8d010648b0aa","http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e", "http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d42"],
#     "grossWeight": "1450",
#     "id": "http://localhost:8080/logistics-objects/a4e59468-2b17-4fcc-93f6-e3518cb0597f" 
#   },
#   "piece17": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0c931213-7fc3-4264-8a01-da0ab1a2711c","http://localhost:8080/logistics-objects/1bdd35b5-d51d-4460-ae0d-4644d7794c49","http://localhost:8080/logistics-objects/5844181f-e932-4133-a250-a849771ade6a","http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d40", "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e4"],
#     "grossWeight": "1309",
#     "id": "http://localhost:8080/logistics-objects/fc26f406-eb4b-430f-8210-8cb73ad2c31e" 
#   },
#   "piece18": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/e1f8e40c-dd8d-43ec-ae10-2863f04ac2c1","http://localhost:8080/logistics-objects/d9abe475-9844-4599-af49-b162cec4c14d","http://localhost:8080/logistics-objects/832e85f2-3701-44fa-8c04-22f279f385c1","http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d49", "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e3"],
#     "grossWeight": "1050",
#     "id": "http://localhost:8080/logistics-objects/c746fbeb-9598-442a-907d-9dbc9f6c4dce" 
#   },
#   "piece19": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0c931213-7fc3-4264-8a01-da0ab1a2711c","http://localhost:8080/logistics-objects/880af942-d48f-4b6a-a8c7-9a7a55c6375d","http://localhost:8080/logistics-objects/bfd7b0d1-98b2-41cb-a378-1a6d707c625a","http://localhost:8080/logistics-objects/1a007384-058e-413f-9865-7f3f218a89d44", "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e0"],
#     "grossWeight": "1208",
#     "id": "http://localhost:8080/logistics-objects/6d1a971d-a243-44de-a9e3-e1009d925288" 
#   },
#   "piece20": {
#     "contentProducts": ["http://localhost:8080/logistics-objects/0600023b-c822-4ee4-a89e-a30030fa7535","http://localhost:8080/logistics-objects/0ea48b9a-c152-47cc-a370-353c57535c79","http://localhost:8080/logistics-objects/b9f4889f-fc13-4375-97fa-2b25b3e2d575","http://localhost:8080/logistics-objects/bfd7b0d1-98b2-41cb-a378-1a6d707c625a","http://localhost:8080/logistics-objects/5844181f-e932-4133-a250-a849771ade6a","http://localhost:8080/logistics-objects/29f41c6d-2d4a-4566-8a64-bc1a45e0af85","http://localhost:8080/logistics-objects/2226d445-e1cc-4600-94c5-49ec57520f83", "http://localhost:8080/logistics-objects/b5c525f8-816d-478f-a77d-956ee4aa660e5"],
#     "grossWeight": "1150",
#     "id": "http://localhost:8080/logistics-objects/2d788ea9-6d4e-44c4-87b8-98539f9f9b92" 
#   }
# }

# for piece in pieces:
#   print("\n----------------------")
#   print(piece)
#   obj = pieces[piece]
#   s = '''
#     {
#       "@context": {
#         "cargo": "https://onerecord.iata.org/ns/cargo#"
#       },
#       "cargo:totalGrossWeight": {
#         "@type": "cargo:Value",
#         "cargo:unit": "KG",
#         "cargo:numericalValue": %s
#       },
#       "@type": "cargo:Piece",
#       "cargo:coload": true,
#       "cargo:goodsDescription": "Some goods",
#       "cargo:upid": "FF-029381-0",
#       "cargo:containedItems": [''' % (obj["grossWeight"])
  
#   for id in obj["contentProducts"]:
#     s += '\n"' + id + '",'
#   s = s[:-1]
#   s += '''
#       ]'''

#   if random.random() > 0.4: # 有特货
#     s += ',\n\t"cargo:handlingInstructions": ['
#     nums = [5,1,1,1,1,1,1,1,1,2,2,2,3,3,4]
#     num = random.choice(nums) # 个数
#     iList = random.sample(range(0, 5),num)
#     for i in iList:
#       sph = sphs[i]
#       s += '''
#         {
#           "@type": "cargo:HandlingInstructions",
#           "cargo:serviceType": "SPH",
#           "cargo:serviceDescription": "%s",
#           "cargo:serviceTypeCode": "%s"
#         },''' % (sph['cargo:serviceDescription'], sph['cargo:serviceTypeCode'])
#     s = s[:-1]
#     s += '''
#       ]'''
#   s += '''
#   }'''
#   print(s)

shipments = {
  "shimpent1": {
    "awbId": "http://localhost:8080/logistics-objects/41092587-c3bb-4b94-8d86-1e8c16e61d23",
    "id": "http://localhost:8080/logistics-objects/4c84ba82-a527-46f0-a452-e02eb6dbd27a"
  },
  "shimpent2": {
    "awbId": "http://localhost:8080/logistics-objects/16d22d95-8c45-475a-aedd-45009ffd1fbb",
    "id": "http://localhost:8080/logistics-objects/406576cb-f7d5-440f-82b1-7857b607ce02"
  },
  "shimpent3": {
    "awbId": "http://localhost:8080/logistics-objects/1e2c07e6-94a8-452c-aa6f-afd73e2b54bf",
    "id": "http://localhost:8080/logistics-objects/07146632-848b-467a-9aad-88307aee59eb"
  },
  "shimpent4": {
    "awbId": "http://localhost:8080/logistics-objects/b04cc4a3-9111-4583-b3c7-9492b02f6bda",
    "id": "http://localhost:8080/logistics-objects/edd891cc-0f6e-4bbb-908d-23e17007e64e"
  },
  "shimpent5": {
    "awbId": "http://localhost:8080/logistics-objects/602675d5-10f7-43d0-b490-1e102adf9657",
    "id": "http://localhost:8080/logistics-objects/edcfc8b2-1a35-440f-b1ed-36a55b894823"
  },
  "shimpent6": {
    "awbId": "http://localhost:8080/logistics-objects/36294f42-8b05-42f8-8c58-5860ca7836fe",
    "id": "http://localhost:8080/logistics-objects/5eed4dce-bc4b-4bce-be45-719ea71f9980"
  },
  "shimpent7": {
    "awbId": "http://localhost:8080/logistics-objects/1de34004-0cdc-4733-885a-a6726de4153e",
    "id": "http://localhost:8080/logistics-objects/d0e720d6-9555-421b-bddc-ddc711c3cfb1"
  },
  "shimpent8": {
    "awbId": "http://localhost:8080/logistics-objects/4a7d585f-ecd5-4b36-a506-a9a8812882ea",
    "id": "http://localhost:8080/logistics-objects/6c9aa4cf-034b-4b88-ad9f-2ebafac8c1f5"
  }
  
}


waybills = {
  "waybill1": {
    "pieces": [
        "http://localhost:8080/logistics-objects/103cf0fb-868e-41d0-96ce-d601b10de136"
      ],
      "awb": "",
    },
  "waybill2": {
    "pieces": [
      "http://localhost:8080/logistics-objects/745fdfc8-d8b5-42c1-802d-b28fb9aff8d6", 
      "http://localhost:8080/logistics-objects/83ed91ee-2b6d-40eb-80c2-4824007965e1", 
      "http://localhost:8080/logistics-objects/a4e2b28f-e47d-45b9-85c5-90605e3e3107",
      "http://localhost:8080/logistics-objects/d67da3bf-d718-4306-b5f1-e1f11a77a4cb"
      ], 
      "awb": ""
      },
  "waybill3": {
    "pieces":[
      "http://localhost:8080/logistics-objects/aa8d9022-e962-4ca0-b948-861cde36caa6"
      ], 
      "awb": ""
      },
  "waybill4": {
    "pieces":[
      "http://localhost:8080/logistics-objects/1ed09d5e-aece-457f-ab4c-6ac5abc95c2d", 
      "http://localhost:8080/logistics-objects/d6393bee-38e0-4c42-923e-a5cb0eaa1d2f", 
      "http://localhost:8080/logistics-objects/5ce75683-415a-4177-bc18-bd358a56b124", 
      "http://localhost:8080/logistics-objects/7d13e2ab-7489-43cd-bf7f-af6f8b94d8fe"
      ],
      "awb": ""
      },
  "waybill5": {
    "pieces":[
      "http://localhost:8080/logistics-objects/559bdc8e-c635-4391-b7f3-8f5bfa0e183b", 
      "http://localhost:8080/logistics-objects/98ed5abf-6317-43b9-adce-4e69734584f1"
      ], 
      "awb": ""
      },
  "waybill6": {
    "pieces":[
      "http://localhost:8080/logistics-objects/c841a3af-74b6-4c20-a733-bcd7970d872d"
      ], 
      "awb": ""
      },
  "waybill7": {
    "pieces":[
      "http://localhost:8080/logistics-objects/51c37027-e11c-4777-8ba7-bd6fc3e33102", 
      "http://localhost:8080/logistics-objects/776b8599-530e-4b3b-a2e9-b12bbc246a75", 
      "http://localhost:8080/logistics-objects/a4e59468-2b17-4fcc-93f6-e3518cb0597f"
      ], 
      "awb": ""
      },
  "waybill8": {
    "pieces":[
      "http://localhost:8080/logistics-objects/fc26f406-eb4b-430f-8210-8cb73ad2c31e", 
      "http://localhost:8080/logistics-objects/c746fbeb-9598-442a-907d-9dbc9f6c4dce", 
      "http://localhost:8080/logistics-objects/6d1a971d-a243-44de-a9e3-e1009d925288", 
      "http://localhost:8080/logistics-objects/2d788ea9-6d4e-44c4-87b8-98539f9f9b92"
      ], 
      "awb": ""
    }
}


# counter = 1
# for key in waybills:
#   waybill = waybills[key]
#   s = '''
#   {
#     "@type": [
#         "LogisticsObject",
#         "Shipment"
#     ],
#     "goodsDescription": "Some goods %d",
#     "pieces": [''' % (counter)
#   counter += 1
#   for piece in waybill["pieces"]:
#     s += '''
#       {
#         "@id": "%s"
#       },''' % (piece)
#   s = s[:-1]
  
#   s += '''
#     ],
#     "@context": {
#         "@vocab": "https://onerecord.iata.org/ns/cargo#"
#     }
#   }
#   '''
#   print("\n\n\n" + key + "\n")

#   print(s)


for i in range(1, 9):
  start = 1410 + i * 3
  shipment = shipments["shimpent" + str(i)]
  waybill = waybills["waybill" + str(i)]
  s = '''
  {
    "@graph": [
      {
        "@type": [
            "LogisticsObject",
            "Waybill"
        ],
        "arrivalLocation": {
            "@id": "http://localhost:8080/logistics-objects/airportPEK"
        },
        "departureLocation": {
            "@id": "http://localhost:8080/logistics-objects/airportSZX"
        },
        "shipment": {
            "@id": "%s"
        },
        "waybillNumber": "9000%d",
        "waybillPrefix": "160",
        "waybillType": {
            "@id": "https://onerecord.iata.org/ns/cargo#DIRECT"
        }
      }
    ],
    "@context": {
        "@vocab": "https://onerecord.iata.org/ns/cargo#"
    }
  }
  ''' % (shipment["id"], start)

  print("-----------------------\n\n", i)
  print(s)













