import broadscope_bailian


class DataGenerator:
    def __init__(self):
        self.access_key_id = '**'
        self.access_key_secret = '**'
        self.agent_key = '**'
        self.app_id = '**'
        self.chat_history = []

    def test_third_model_completions(self, input_text):
        """ 三方模型应用示例 """
        f = open("res.txt", "w")
        access_key_id = self.access_key_id
        access_key_secret = self.access_key_secret
        agent_key = self.agent_key
        app_id = self.app_id

        client = broadscope_bailian.AccessTokenClient(access_key_id=access_key_id, access_key_secret=access_key_secret,
                                                      agent_key=agent_key)
        token = client.get_token()

        prompt = input_text
        resp = broadscope_bailian.Completions(token=token).create(
            app_id=app_id,
            prompt=prompt,
            history=self.chat_history,
        )
        if not resp.get("Success"):
            print("failed to create completion, request_id: %s, code: %s, message: %s" %
                  (resp.get("RequestId"), resp.get("Code"), resp.get("Message")))
        else:
            print("request_id: %s, text: %s" % (resp.get("RequestId"), resp.get("Data", {}).get("Text")))
            f.write(resp.get("Data", {}).get("Text") + "\n")
            doc_references = resp.get("Data", {}).get("DocReferences")
            if doc_references is not None and len(doc_references) > 0:
                print("doc ref: %s" % doc_references[0].get("DocName"))
            self.chat_history.append({"user": input_text, "bot": resp.get("Data", {}).get("Text")})

        f.close()


if __name__ == '__main__':
    test = DataGenerator()
    input_text = """
    查询三十个知名品牌
    """
    while input_text != "quit":
        test.test_third_model_completions(input_text)
        input_text = input("please input:\n")
