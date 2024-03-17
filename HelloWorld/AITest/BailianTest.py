import broadscope_bailian


class CompletionTest:
    def __init__(self):
        self.access_key_id = '**'
        self.access_key_secret = '**'
        self.agent_key = '**'
        self.app_id = '**'
        self.chat_history = [
            {"user": "谈谈你对航空货运的理解",
             "bot": """
             航空货运，是指利用各类航空器（如客机、货机等）进行货物运输的一种现代化物流方式。其主要特点是速度快、效率高、安全性强，
             尤其适合于对时间要求严格、价值密度高的货物运输，例如精密仪器、电子产品、鲜活商品、贵重物品、紧急救援物资等。
             1. 时效性：航空货运的最显著优势是运输速度快，能够大大缩短货物在途时间，实现快速响应市场需求，对于国际贸易和供应链管理具有重要意义。
             2. 安全性：航空货运的安全标准较高，货物在机场经过严格的安检流程，且飞行过程中受控程度高，货物损坏或丢失的风险相对较小。
             3. 灵活性：航空货运可以直达全球各地的主要城市，不受地理条件限制，航线网络覆盖面广，能满足不同地区、不同时效需求的货物运输。
             4. 高附加值服务：许多航空公司和货运代理公司提供门到门、一站式、定制化的增值服务，包括货物包装、报关清关、保险理赔等，为客户提供便利。
             然而，航空货运也存在成本相对较高的问题，这主要是由于飞机运营成本、燃油费用以及机场操作费用等因素导致的。因此，在选择货运方式时，
             企业通常需要根据货物的特性、价值、交货期限以及自身的经济承受能力等因素综合考虑。"""},
            {"user": "你对IATA推出的one record 有了解吗",
             "bot": """
             是的，我了解IATA推出的"ONE Record"（单一记录）项目。
             国际航空运输协会（IATA）提出的“ONE Record”是一项旨在推动航空货运行业数字化转型的重大倡议。传统的航空货运流程中，
             货物信息在各个环节被分割存储在不同的系统和文档中，如货运单、报关文件等，这导致了信息交换效率低下，透明度不足，影响了整个供应链的效率和客户体验。
             "ONE Record"的核心理念是将所有与货物运输相关的数据整合到一个统一、共享的数据源中，形成一个完整的、实时更新的数字记录。
             这个单一记录包含了从预订、接收到交付全过程的所有必要信息，包括货物详情、运输条件、费用、清关状态等，
             使得所有参与方（托运人、承运人、地面代理、海关和其他监管机构等）都能访问并操作同一份准确、实时的信息，从而显著提升物流效率，减少错误和延误，降低成本，并增强货物的安全性和可追溯性。
             通过实施"ONE Record"，航空货运业有望实现真正的端到端数字化，为全球贸易提供更为高效、便捷的服务。"""},
            {"user": "那你认为航空货运中影响货物优先级的因素有哪些",
             "bot": """
             航空货运中，货物的优先级通常受到以下因素的影响：
             1. **交货时间要求**：如果货物有严格的交货期限或紧急程度高，例如鲜活易腐商品、急需的医疗设备或关键零部件等，这类货物往往会获得更高的运输优先级。
             2. **货物价值**：货物的价值密度也会影响其优先级。高价值物品如珠宝、艺术品、精密仪器等，由于其经济价值和潜在损失风险较大，承运方可能会给予更高优先级以确保安全准时送达。
             3. **货物性质**：某些特殊性质的货物，如危险品、贵重物品、外交邮袋等，因其特殊的处理要求和法规限制，可能需要优先安排运输。
             4. **客户级别和服务协议**：对于长期合作且签订了高级服务协议的客户，其货物可能会享受优先运输待遇。此外，VIP客户或者具有战略意义的大客户，他们的货物也可能被赋予较高优先级。
             5. **航班舱位情况**：在实际操作中，航班剩余舱位也是影响货物优先级的一个重要因素。当舱位紧张时，航空公司会根据货物的重要性和紧急程度来决定装载顺序。
             6. **季节性及市场供需关系**：在特定的季节或市场环境下，如节假日购物季、疫情等特殊情况，部分货物（如电商产品、防疫物资）的需求量剧增，这些货物的运输优先级也会相应提高。
             综上所述，航空货运中的货物优先级是一个综合考量多种因素的结果，旨在优化资源配置，满足不同客户的需求，并确保整个物流链的高效运作。"""},
            {
                "user": "我希望你能将货物的价值理解成货物的毛利，因为高价值物品的运输成本比较高，与之对应的优先级反而有可能降低，现在请重新给予我你对航空货运中影响货物优先级因素的排序",
                "bot": """
             理解您的修正，将货物价值理解为“货物毛利”后，确实高运输成本可能会影响高价值物品的优先级。在航空货运中，影响货物优先级的因素可以重新排序如下：
             1. **交货时间要求**：紧急程度和时效性始终是决定货物优先级的首要因素，无论货物的成本如何，对于有严格交货期限或时间敏感性的货物，如鲜活易腐品、紧急医疗设备等，其优先级通常最高。
             2. **货物性质与法规要求**：特殊货物如危险品、贵重物品、外交邮袋等因其特殊的处理规定和法规限制，必须按照特定流程进行操作，这也会直接影响其优先级。
             3. **客户级别和服务协议**：长期合作且签订了高级服务协议的客户，或者VIP客户，他们的货物可能会根据合同约定享有优先权。
             4. **航班舱位情况与装载效率**：实际运营中，航班剩余舱位及装载顺序对货物优先级也有重要影响，航空公司会根据货物尺寸、重量以及飞机平衡等因素综合考虑装载顺序。
             5. **货物毛利与运输成本效益分析**：虽然高毛利货物的运输成本可能较高，但在充分考虑运输成本与预期收益之间的平衡后，如果货物的预期利润足以覆盖高昂的运输成本，
                并且及时送达能带来更大的商业价值，那么这类货物仍有可能获得较高的运输优先级。然而，在实际操作中，由于运输成本的影响，此类货物的优先级可能会相对降低，需要具体情况具体分析。
             6. **季节性及市场供需关系**：在特定时期内，市场需求旺盛的货物（如节假日商品、热点产品）也可能因市场供需关系而获得较高的运输优先级。"""},
            {
                "user": "因为one reocrd的数据中没有服务协议和市场供需关系的相关数据，希望你去掉这两个因素后，提出新的角度，重新进行你对航空货运中影响货物优先级因素的排序",
                "bot": """理解您的要求，基于"One Record"数据中可能包含的信息，排除服务协议和市场供需关系后，影响航空货运中货物优先级的因素可以重新排序如下：
             1. **交货时间要求**：货物的运输紧急程度和时效性仍然是决定其优先级的关键因素。在"One Record"数据中，可以通过预定的运输时间和实际需求到达时间来判断货物的紧急程度。
             2. **货物性质与法规要求**：根据"One Record"中的货物描述、分类和其他相关属性信息，可以确定货物是否为特殊货物（如危险品、贵重物品等），这些货物由于处理规定和法规限制，通常具有较高的运输优先级。
             3. **货物重量与体积**：在"One Record"数据中，货物的重量和体积信息直接影响飞机的装载计划和平衡控制，对于大型或重型货物，可能会因其对航班运营的影响而获得较高优先级。
             4. **货物价值（毛利）与运输成本效益分析**：虽然"One Record"可能不直接包含货物的毛利信息，但可以根据运费、保险费等相关费用推断出货物的价值重要性。高价值且能承受较高运输成本的货物，在权衡成本效益后，仍可能获得一定的优先考虑。
             5. **航班舱位情况与装载效率**：通过"One Record"系统可以实时了解航班舱位状况，以便合理安排货物装载顺序，提高装载效率，这也会影响货物的实际运输优先级。
             6. **货物状态与安全风险**：如果"One Record"中包含了货物的状态信息（如鲜活易腐、需恒温恒湿保存等），这类货物因对运输条件有特殊要求，会因其安全风险和保障需求而被赋予较高优先级。"""},
            {
                "user": "很好，由于在理想情况下，货机的配重情况不参与对货运优先级的影响，以及one record中，也没有对于航班舱位和装载效率的相关数据，希望你重新进行你对航空货运中影响货物优先级因素的排序",
                "bot": """理解您的要求，基于"One Record"系统可能提供的信息，并排除货机配重情况和航班舱位及装载效率的影响因素后，航空货运中影响货物优先级的因素可以重新排序如下：
             1. **交货时间要求**：货物的运输紧急程度和时效性仍然是决定其优先级的核心要素。通过"One Record"中的预定运输时间和实际需求到达时间来判断货物是否需要优先处理。
             2. **货物性质与法规要求**：根据"One Record"记录的货物类型、特殊属性（如危险品、贵重物品、易腐品等）以及相关法规要求，这些货物通常具有较高的运输优先级。
             3. **货物状态与安全风险**：如果"One Record"包含货物的状态信息（如鲜活易腐、需特殊环境保存等），这类货物因其对运输条件有特殊要求，且存在较高的安全风险，因此在考虑优先级时会得到重视。
             4. **货物价值（毛利）与运输成本效益分析**：虽然"One Record"不直接提供货物毛利数据，但可以根据运费、保险费等相关费用推断出货物的价值重要性。对于高价值且能承受较高运输成本的货物，在权衡成本效益后，仍可能获得一定的优先级考量。
             5. **客户历史行为与信用等级**：虽然"One Record"可能不直接体现服务协议，但可以通过分析客户的过往交易记录、支付信誉等因素，间接影响到货物的处理优先级。
             6. **货物目的地与航线安排**：在"One Record"中，货物的目的地信息可以帮助航空公司或承运方结合航线计划和航班时刻表，合理安排货物的运输顺序，从而间接影响货物的优先级。"""},
            {
                "user": "很好，希望你把客户历史行为与信用等级理解成客户关系，假如，客户拥有长期合作关系，也应算入影响优先级的因素，将这一点替换后，再请你重新进行你对航空货运中影响货物优先级因素的排序",
                "bot": """
             理解您的修正，将“客户历史行为与信用等级”替换为“客户关系”，基于"One Record"系统可能提供的信息，并排除货机配重情况和航班舱位及装载效率的影响因素后，航空货运中影响货物优先级的因素可以重新排序如下：
             1. **交货时间要求**：货物的运输紧急程度和时效性仍然是决定其优先级的关键因素，通过"One Record"中的预定运输时间和实际需求到达时间来判断。
             2. **货物性质与法规要求**：根据"One Record"记录的货物类型、特殊属性（如危险品、贵重物品、易腐品等）以及相关法规要求，这些货物通常具有较高的运输优先级。
             3. **客户关系**：长期合作且具有良好合作关系的客户，他们的货物可能会因为商业信誉和合同约定等因素而获得更高的运输优先级。即使在"One Record"系统中不直接体现，航空公司或承运方也会依据客户关系进行优先级调整。
             4. **货物状态与安全风险**：如果"One Record"包含货物的状态信息（如鲜活易腐、需特殊环境保存等），这类货物因其对运输条件有特殊要求且存在较高安全风险，因此在考虑优先级时会得到重视。
             5. **货物价值（毛利）与运输成本效益分析**：虽然"One Record"不直接提供货物毛利数据，但可以根据运费、保险费等相关费用推断出货物的价值重要性。对于高价值且能承受较高运输成本的货物，在权衡成本效益后，仍可能影响其优先级。
             6. **货物目的地与航线安排**：货物的目的地信息结合航线计划和航班时刻表，可以帮助合理安排货物运输顺序，间接影响货物的优先级。"""
                },
            {"user": """
             现在给你几组货单，数据可能会包括前缀、货单号、起运站、到达站、代理人号、货物产品服务、特货代码、计费重量、货币、运价（你可以理解成单价）、运费、成本、每公斤毛利的相关信息，
             其中，特货代码不是NA的，意味着它是危险品或者活体动物运输（如AVI是活体动物；PER为鲜活易腐），请据此酌情判断货物的时效性；
             货物产品服务为EXP的，意味着对运输时效性要求很高，请根据我后续给出的货物信息给出你对于所有货物的优先级排序""",
             "bot": """理解您的描述，基于您提供的货单信息，我们可以根据以下因素对货物优先级进行排序：
             1. **运输时效性要求**：
                - 货物产品服务为“EXP”（表示快递或紧急运输），这类货物应被赋予最高优先级。
                - 特货代码不为空且非“NA”，意味着是危险品或活体动物运输，此类货物由于其特殊性质和法规要求，通常需要快速、安全地处理，因此也应具有较高优先级。
             2. **货物价值与毛利**：
                - 根据运费、成本以及每公斤毛利的数据，可以计算出货物的总毛利。高毛利且能承受较高运输成本的货物，在满足其他条件的情况下，可适当提高其优先级。
             3. **起运站与到达站**：
                - 如果某些航线或目的地存在航班频次限制或者通关效率差异，可能会影响货物的实际送达时间，因此在考虑时效性的同时，也需要结合起运站和到达站的具体情况来调整优先级。
             4. **计费重量**：
                - 对于大型或重型货物，虽然它们可能对飞机装载有特定要求，但在实际操作中，如果其运输时效性和价值都较高，那么仍应给予较高的优先级。
             综合以上因素，建议按照以下顺序排列货物优先级：
             1. 货物产品服务为“EXP”的货物，同时考虑特货代码是否代表危险品或活体动物运输。
             2. 在满足上述条件的基础上，进一步比较货物的每公斤毛利，毛利高的货物优先级提升。
             3. 结合起运站和到达站的航班安排及实际情况微调优先级。
             4. 若计费重量对航班装载有显著影响，但时效性和价值均较高的货物，依然保持相对较高的优先级。
             请注意，实际操作中还需结合航空公司或承运方的具体政策和资源分配情况来最终确定货物的优先级。
            """}
        ]
        self.prompt = """
            现在，给你一组数据，你可以看作是一张货单（awb）内包含的所有的pieces的信息，
            每一个piece的格式都是相同的，但包含的字段数量可能不同，如果存在相同含义的字段结果为空，请忽略。
            它们中的每一个字段都有相应的含义，解释如下：
                awbId是piece和awb的映射关系。
                awbNum是货单号。
                cost是成本数据，
                price是收入数据，
                unitProfit是每公斤毛利，
                忽略goodsDescription和它携带的内容，
                handlingInstructions即为特货代码或货物产品服务，
                其中包括VAL（高价值货物），AAA（最高优先级货物），AVI（活体动物），PER（鲜活易腐货物），CCV（新冠疫苗相关货物）
                grossWeight是毛重数据，
                products这个key是对应着这个piece的具体的货物描述，你可以根据它酌情考虑货物的优先级，
                当然，需要注意的是，一个piece中通常包括不止一种货物，需要你对货物的描述进行理解。
            
            请给出你对piece（也就是货物优先级）的排序和解释，尽可能根据货物的描述、特货代码和每公斤毛利给出你的建议。
            数据输出格式要求如下：
            1. pieces的顺序要按照由piece的优先级由高到低排序。
            2. 格式为：
            [{"pieceId": 你的解释}, {"pieceId": 你的解释}...]
            3. 除了写在json内的解释，不要再多余进行注释
            
            示例如下：
                [
                    {
                        "awbId": "602675d5-10f7-43d0-b490-1e102adf9657",
                        "awbNum": "160-90001425",
                        "cost": 1582,
                        "price": 3366,
                        "unitProfit": 55,
                        "pieceId": "559bdc8e-c635-4391-b7f3-8f5bfa0e183b",
                        "grossWeight": 32,
                        "goodsDescription": "Some goods 5",
                        "handlingInstructions": [
                            "AVI"
                        ],
                        "products": [
                            {
                                "description": "Food and Beverage Products in Bulk Quantity"
                            },
                            {
                                "description": "Household and Personal Care Product Cargo"
                            },
                            {
                                "description": "ThinkPad Laptops and Desktop Computers Shipment"
                            },
                            {
                                "description": "Cola Beverages in Industrial Quantities"
                            },
                            {
                                "description": "Licensed Merchandise and Toys Container"
                            },
                            {
                                "description": "Bottled Soft Drinks in Bulk Cases"
                            }
                        ]
                    },
                    {
                        "awbId": "602675d5-10f7-43d0-b490-1e102adf9657",
                        "awbNum": "160-90001425",
                        "cost": 1582,
                        "price": 3366,
                        "unitProfit": 55,
                        "pieceId": "98ed5abf-6317-43b9-adce-4e69734584f1",
                        "grossWeight": 31,
                        "goodsDescription": "Some goods 5",
                        "handlingInstructions": [
                            "CCV",
                            "PER",
                            "VAL"
                        ],
                        "products": [
                            {
                                "description": "Household and Personal Care Product Cargo"
                            },
                            {
                                "description": "Skincare and Makeup Products Batch"
                            },
                            {
                                "description": "Auto Parts and Components Transport"
                            },
                            {
                                "description": "Cola Beverages in Industrial Quantities"
                            },
                            {
                                "description": "Cosmetics and Haircare Products Shipment"
                            },
                            {
                                "description": "Leather Handbags in Master Cartons"
                            }
                        ]
                    }
                ]
                输出应为：
                [{"98ed5abf-6317-43b9-adce-4e69734584f1":"我认为尽管两个piece的每公斤毛利相同，但由于第二个piece涉及新冠疫苗、鲜活易腐品及高价值货物，
                其优先级应高于第一个piece"},
                {"559bdc8e-c635-4391-b7f3-8f5bfa0e183b":"考虑到特货代码不同，我认为第一个piece优先级可以适当降低"}]}"""

    def test_third_model_completions(self, input_text):
        access_key_id = self.access_key_id
        access_key_secret = self.access_key_secret
        agent_key = self.agent_key
        app_id = self.app_id

        client = broadscope_bailian.AccessTokenClient(access_key_id=access_key_id, access_key_secret=access_key_secret,
                                                      agent_key=agent_key)
        token = client.get_token()
        prompt = f"""{self.prompt}
        ===================================
        上下文：
        {input_text}
        输出："""
        resp = broadscope_bailian.Completions(token=token).create(
            app_id=app_id,
            prompt=prompt,
            history=self.chat_history,
        )

        if not resp.get("Success"):
            print("failed to create completion, request_id: %s, code: %s, message: %s" %
                  (resp.get("RequestId"), resp.get("Code"), resp.get("Message")))
        else:
            # print("request_id: %s, text: %s" % (resp.get("RequestId"), resp.get("Data", {}).get("Text")))
            doc_references = resp.get("Data", {}).get("DocReferences")
            # if doc_references is not None and len(doc_references) > 0:
            #     print("doc ref: %s" % doc_references[0].get("DocName"))
            self.chat_history.append({"user": input_text, "bot": resp.get("Data", {}).get("Text")})
            return resp.get("Data", {}).get("Text")


if __name__ == '__main__':
    test = CompletionTest()
    input_text = """
    [
    {
        "awbId": "41092587-c3bb-4b94-8d86-1e8c16e61d23",
        "awbNum": "160-90001413",
        "cost": 382,
        "price": 850,
        "pieceId": "103cf0fb-868e-41d0-96ce-d601b10de136",
        "grossWeight": 25,
        "goodsDescription": "Some goods 1",
        "handlingInstructions": [],
        "products": [
            {
                "description": "Performance Sportswear and Shoes Crate"
            },
            {
                "description": "PlayStation Consoles and Bravia TVs Box"
            },
            {
                "description": "Food and Beverage Products in Bulk Quantity"
            },
            {
                "description": "Shoeboxes of Air Jordan Sneakers"
            },
            {
                "description": "Automotive Spare Parts Containers"
            }
        ],
        "unitProfit": 18
    },
    {
        "awbId": "16d22d95-8c45-475a-aedd-45009ffd1fbb",
        "awbNum": "160-90001416",
        "cost": 793,
        "price": 1280,
        "pieceId": "745fdfc8-d8b5-42c1-802d-b28fb9aff8d6",
        "grossWeight": 35,
        "goodsDescription": "Some goods 2",
        "handlingInstructions": [],
        "products": [
            {
                "description": "Performance Sportswear and Shoes Crate"
            },
            {
                "description": "Household and Personal Care Product Cargo"
            },
            {
                "description": "Consumer Products and Personal Care Goods Load"
            },
            {
                "description": "ThinkPad Laptops and Desktop Computers Shipment"
            }
        ],
        "unitProfit": 4
    },
    {
        "awbId": "16d22d95-8c45-475a-aedd-45009ffd1fbb",
        "awbNum": "160-90001416",
        "cost": 793,
        "price": 1280,
        "pieceId": "83ed91ee-2b6d-40eb-80c2-4824007965e1",
        "grossWeight": 30,
        "goodsDescription": "Some goods 2",
        "handlingInstructions": [],
        "products": [
            {
                "description": "Xbox Consoles and Surface Tablets Shipment"
            },
            {
                "description": "Household and Personal Care Product Cargo"
            },
            {
                "description": "Consumer Products and Personal Care Goods Load"
            },
            {
                "description": "Auto Parts and Components Transport"
            }
        ],
        "unitProfit": 4
    },
    {
        "awbId": "16d22d95-8c45-475a-aedd-45009ffd1fbb",
        "awbNum": "160-90001416",
        "cost": 793,
        "price": 1280,
        "pieceId": "a4e2b28f-e47d-45b9-85c5-90605e3e3107",
        "grossWeight": 24,
        "goodsDescription": "Some goods 2",
        "handlingInstructions": [
            "CCV",
            "AAA"
        ],
        "products": [
            {
                "description": "Performance Sportswear and Shoes Crate"
            },
            {
                "description": "PlayStation Consoles and Bravia TVs Box"
            },
            {
                "description": "Skincare and Makeup Products Batch"
            },
            {
                "description": "Flat-Packed Furniture and Home Decor Items Crate"
            },
            {
                "description": "Fast-Fashion Garments and Accessories Bundle"
            }
        ],
        "unitProfit": 4
    },
    {
        "awbId": "16d22d95-8c45-475a-aedd-45009ffd1fbb",
        "awbNum": "160-90001416",
        "cost": 793,
        "price": 1280,
        "pieceId": "d67da3bf-d718-4306-b5f1-e1f11a77a4cb",
        "grossWeight": 16,
        "goodsDescription": "Some goods 2",
        "handlingInstructions": [],
        "products": [
            {
                "description": "Performance Sportswear and Shoes Crate"
            },
            {
                "description": "Xbox Consoles and Surface Tablets Shipment"
            },
            {
                "description": "Household and Personal Care Product Cargo"
            },
            {
                "description": "Coffee Beans and Retail Store Supplies Package"
            },
            {
                "description": "Skincare and Makeup Products Batch"
            }
        ],
        "unitProfit": 4
    },
    {
        "awbId": "1e2c07e6-94a8-452c-aa6f-afd73e2b54bf",
        "awbNum": "160-90001419",
        "cost": 1303,
        "price": 2370,
        "pieceId": "aa8d9022-e962-4ca0-b948-861cde36caa6",
        "grossWeight": 34,
        "goodsDescription": "Some goods 3",
        "handlingInstructions": [],
        "products": [
            {
                "description": "Performance Sportswear and Shoes Crate"
            },
            {
                "description": "Skincare and Makeup Products Batch"
            }
        ],
        "unitProfit": 31
    },
    {
        "awbId": "b04cc4a3-9111-4583-b3c7-9492b02f6bda",
        "awbNum": "160-90001422",
        "cost": 1663,
        "price": 2160,
        "pieceId": "5ce75683-415a-4177-bc18-bd358a56b124",
        "grossWeight": 25,
        "goodsDescription": "Some goods 4",
        "handlingInstructions": [
            "PER",
            "VAL",
            "CCV"
        ],
        "products": [
            {
                "description": "PlayStation Consoles and Bravia TVs Box"
            },
            {
                "description": "Coffee Beans and Retail Store Supplies Package"
            },
            {
                "description": "ThinkPad Laptops and Desktop Computers Shipment"
            },
            {
                "description": "Auto Parts and Components Transport"
            },
            {
                "description": "Mate Series Smartphones and Laptops Pallet"
            }
        ],
        "unitProfit": 2
    },
    {
        "awbId": "b04cc4a3-9111-4583-b3c7-9492b02f6bda",
        "awbNum": "160-90001422",
        "cost": 1663,
        "price": 2160,
        "pieceId": "1ed09d5e-aece-457f-ab4c-6ac5abc95c2d",
        "grossWeight": 32,
        "goodsDescription": "Some goods 4",
        "handlingInstructions": [],
        "products": [
            {
                "description": "PlayStation Consoles and Bravia TVs Box"
            },
            {
                "description": "Xbox Consoles and Surface Tablets Shipment"
            },
            {
                "description": "Fast-Fashion Garments and Accessories Bundle"
            },
            {
                "description": "Electric Vehicle Components and Batteries Shipment"
            }
        ],
        "unitProfit": 2
    },
    {
        "awbId": "b04cc4a3-9111-4583-b3c7-9492b02f6bda",
        "awbNum": "160-90001422",
        "cost": 1663,
        "price": 2160,
        "pieceId": "d6393bee-38e0-4c42-923e-a5cb0eaa1d2f",
        "grossWeight": 78,
        "goodsDescription": "Some goods 4",
        "handlingInstructions": [
            "CCV",
            "PER",
            "AVI",
            "AAA"
        ],
        "products": [
            {
                "description": "Performance Sportswear and Shoes Crate"
            },
            {
                "description": "PlayStation Consoles and Bravia TVs Box"
            },
            {
                "description": "Electric Vehicle Components and Batteries Shipment"
            },
            {
                "description": "Computer Processors and Chips Consignment"
            }
        ],
        "unitProfit": 2
    },
    {
        "awbId": "b04cc4a3-9111-4583-b3c7-9492b02f6bda",
        "awbNum": "160-90001422",
        "cost": 1663,
        "price": 2160,
        "pieceId": "7d13e2ab-7489-43cd-bf7f-af6f8b94d8fe",
        "grossWeight": 45,
        "goodsDescription": "Some goods 4",
        "handlingInstructions": [],
        "products": [
            {
                "description": "Xbox Consoles and Surface Tablets Shipment"
            },
            {
                "description": "ThinkPad Laptops and Desktop Computers Shipment"
            },
            {
                "description": "Flat-Packed Furniture and Home Decor Items Crate"
            },
            {
                "description": "Cola Beverages in Industrial Quantities"
            },
            {
                "description": "Car Components and Accessories Freight"
            },
            {
                "description": "Designer Clothing and Accessories Parcel"
            },
            {
                "description": "A-Class Sedan Auto Parts Shipment"
            }
        ],
        "unitProfit": 2
    },
    {
        "awbId": "602675d5-10f7-43d0-b490-1e102adf9657",
        "awbNum": "160-90001425",
        "cost": 1582,
        "price": 3366,
        "pieceId": "559bdc8e-c635-4391-b7f3-8f5bfa0e183b",
        "grossWeight": 32,
        "goodsDescription": "Some goods 5",
        "handlingInstructions": [
            "AVI"
        ],
        "products": [
            {
                "description": "Food and Beverage Products in Bulk Quantity"
            },
            {
                "description": "Household and Personal Care Product Cargo"
            },
            {
                "description": "ThinkPad Laptops and Desktop Computers Shipment"
            },
            {
                "description": "Cola Beverages in Industrial Quantities"
            },
            {
                "description": "Licensed Merchandise and Toys Container"
            },
            {
                "description": "Bottled Soft Drinks in Bulk Cases"
            }
        ],
        "unitProfit": 28
    },
    {
        "awbId": "602675d5-10f7-43d0-b490-1e102adf9657",
        "awbNum": "160-90001425",
        "cost": 1582,
        "price": 3366,
        "pieceId": "98ed5abf-6317-43b9-adce-4e69734584f1",
        "grossWeight": 31,
        "goodsDescription": "Some goods 5",
        "handlingInstructions": [
            "CCV",
            "PER",
            "VAL"
        ],
        "products": [
            {
                "description": "Household and Personal Care Product Cargo"
            },
            {
                "description": "Skincare and Makeup Products Batch"
            },
            {
                "description": "Auto Parts and Components Transport"
            },
            {
                "description": "Cola Beverages in Industrial Quantities"
            },
            {
                "description": "Cosmetics and Haircare Products Shipment"
            },
            {
                "description": "Leather Handbags in Master Cartons"
            }
        ],
        "unitProfit": 28
    },
    {
        "awbId": "36294f42-8b05-42f8-8c58-5860ca7836fe",
        "awbNum": "160-90001428",
        "cost": 621,
        "price": 1002,
        "pieceId": "c841a3af-74b6-4c20-a733-bcd7970d872d",
        "grossWeight": 56,
        "goodsDescription": "Some goods 6",
        "handlingInstructions": [],
        "products": [
            {
                "description": "Xbox Consoles and Surface Tablets Shipment"
            },
            {
                "description": "Coffee Beans and Retail Store Supplies Package"
            },
            {
                "description": "Mate Series Smartphones and Laptops Pallet"
            },
            {
                "description": "Computer Processors and Chips Consignment"
            },
            {
                "description": "Cola Beverages in Industrial Quantities"
            },
            {
                "description": "Licensed Merchandise and Toys Container"
            },
            {
                "description": "Cosmetics and Haircare Products Shipment"
            },
            {
                "description": "Galaxy Smartphone Inventory Lot"
            }
        ],
        "unitProfit": 6
    },
    {
        "awbId": "1de34004-0cdc-4733-885a-a6726de4153e",
        "awbNum": "160-90001431",
        "cost": 1771,
        "price": 4120,
        "pieceId": "51c37027-e11c-4777-8ba7-bd6fc3e33102",
        "grossWeight": 34,
        "goodsDescription": "Some goods 7",
        "handlingInstructions": [],
        "products": [
            {
                "description": "Cola Beverages in Industrial Quantities"
            },
            {
                "description": "Licensed Merchandise and Toys Container"
            },
            {
                "description": "Perfumes, Cosmetics and Fashion Goods Bundle"
            },
            {
                "description": "Kindle E-Readers and Echo Devices Cargo"
            },
            {
                "description": "Frozen Food and Packaging Supplies"
            }
        ],
        "unitProfit": 12
    },
    {
        "awbId": "1de34004-0cdc-4733-885a-a6726de4153e",
        "awbNum": "160-90001431",
        "cost": 1771,
        "price": 4120,
        "pieceId": "776b8599-530e-4b3b-a2e9-b12bbc246a75",
        "grossWeight": 89,
        "goodsDescription": "Some goods 7",
        "handlingInstructions": [
            "VAL"
        ],
        "products": [
            {
                "description": "Consumer Products and Personal Care Goods Load"
            },
            {
                "description": "Electric Vehicle Components and Batteries Shipment"
            },
            {
                "description": "Licensed Merchandise and Toys Container"
            },
            {
                "description": "Car Components and Accessories Freight"
            },
            {
                "description": "Perfumes, Cosmetics and Fashion Goods Bundle"
            }
        ],
        "unitProfit": 12
    },
    {
        "awbId": "4a7d585f-ecd5-4b36-a506-a9a8812882ea",
        "awbNum": "160-90001434",
        "cost": 3054,
        "price": 4773,
        "pieceId": "c746fbeb-9598-442a-907d-9dbc9f6c4dce",
        "grossWeight": 56,
        "goodsDescription": "Some goods 8",
        "handlingInstructions": [
            "VAL"
        ],
        "products": [
            {
                "description": "Electric Vehicle Components and Batteries Shipment"
            },
            {
                "description": "Designer Clothing and Accessories Parcel"
            },
            {
                "description": "Perfumes, Cosmetics and Fashion Goods Bundle"
            }
        ],
        "unitProfit": 12
    },
    {
        "awbId": "4a7d585f-ecd5-4b36-a506-a9a8812882ea",
        "awbNum": "160-90001434",
        "cost": 3054,
        "price": 4773,
        "pieceId": "6d1a971d-a243-44de-a9e3-e1009d925288",
        "grossWeight": 23,
        "goodsDescription": "Some goods 8",
        "handlingInstructions": [
            "CCV"
        ],
        "products": [
            {
                "description": "Consumer Products and Personal Care Goods Load"
            },
            {
                "description": "Flat-Packed Furniture and Home Decor Items Crate"
            },
            {
                "description": "Car Components and Accessories Freight"
            }
        ],
        "unitProfit": 12
    },
    {
        "awbId": "4a7d585f-ecd5-4b36-a506-a9a8812882ea",
        "awbNum": "160-90001434",
        "cost": 3054,
        "price": 4773,
        "pieceId": "2d788ea9-6d4e-44c4-87b8-98539f9f9b92",
        "grossWeight": 22,
        "goodsDescription": "Some goods 8",
        "handlingInstructions": [],
        "products": [
            {
                "description": "Food and Beverage Products in Bulk Quantity"
            },
            {
                "description": "Automotive Spare Parts Containers"
            },
            {
                "description": "Xbox Consoles and Surface Tablets Shipment"
            },
            {
                "description": "Coffee Beans and Retail Store Supplies Package"
            },
            {
                "description": "Auto Parts and Components Transport"
            },
            {
                "description": "Flat-Packed Furniture and Home Decor Items Crate"
            },
            {
                "description": "Computer Processors and Chips Consignment"
            }
        ],
        "unitProfit": 12
    }
]
    """
    test.test_third_model_completions(input_text)
