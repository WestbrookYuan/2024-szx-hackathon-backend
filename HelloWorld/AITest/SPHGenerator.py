l = {"VAL":"Valuable Cargo",
     "AAA":"highest priority",
     "AVI":"living animal",
     "CCV":"covid vaccine",
     "PER":"perishable goods"}

template = {
    "@type": "cargo:HandlingInstructions",
    "cargo:serviceType": "SPH",
    "cargo:serviceDescription": "Valuable Cargo",
    "cargo:serviceTypeCode": "VAL"}

res = []

for key in l:
    temp = {}
    for temp_key in template:
        temp[temp_key] = template[temp_key]
        if temp_key == "cargo:serviceTypeCode":
            temp[temp_key] = key
        if temp_key == "cargo:serviceDescription":
            temp[temp_key] = l[key]

    res.append(temp)

for i in res:
    print(i)

print(res)

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

for i in shipments:
    print(shipments[i]["awbId"])