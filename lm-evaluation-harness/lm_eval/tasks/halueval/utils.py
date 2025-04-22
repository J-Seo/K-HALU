# Main reference: https://github.com/RUCAIBox/HaluEval/blob/main/evaluation/evaluate.py

QA_INSTURCTIONS_MT = """I want you act as an answer judge. Given a question and an answer, your objective is to determine if the provided answer contains non-factual or hallucinated information. You SHOULD give your judgement based on the following hallucination types and the world knowledge.

You are trying to translate the knowledge, question, and answer into a different language.
You are trying to determine if the answer misunderstands the question context and intention.
#Question#: What is a rare breed of dog that was derived as a variant of Rat Terrier, Shiloh Shepherd dog or American Hairless Terrier?
#Question_Korean#: 랫 테리어(Rat Terrier), 실로 셰퍼드(Shiloh Shepherd) 또는 아메리칸 헤어리스 테리어(American Hairless Terrier)의 변종으로 파생된 희귀한 개 품종은 무엇인가요?
#Answer#: American Hairless Terrier
#Answer_Korean#: 아메리칸 헤어리스 테리어
#Your Judgement#: No

You are trying to translate the knowledge, question, and answer into a different language.
You are trying to determine if there is a factual contradiction between the answer and the world knowledge. Some information in the answer might be fabricated.
#Knowledge#: The canal is fed by the Savannah River and passes through three levels (approximately 13 miles total) in suburban and urban Augusta before the water returns to the river at various locations. There are 13 mi of levees and floodwalls that line the sides of the canals.
#Knowledge_Korean#: 이 채널은 사반나 강(Savannah River)에서 물을 공급받아 서브버안과 어번 오거스타(Augusta)의 세 단계(약 13마일 총)를 지나 다양한 위치에서 강으로 돌아가는 물이 있습니다. 채널 양쪽에는 13마일의 제방과 방수벽이 있습니다.
#Question#: Are the New Orleans Outfall Canals the same length as the Augusta Canal?
#Question_Korean#: 뉴올리언스 아웃폴 캐널(New Orleans Outfall Canals)과 오거스타 캐널(Augusta Canal)이 같은 길이인가요?
#Answer#: No, the New Orleans Outfall Canals and the Augusta Canal are not the same length. The Orleans Canal is approximately 3.6 miles (5.8 kilometers) long while the Augusta Canal is approximately 7 miles (11.3 kilometers) long.
#Answer_Korean#: 아니요, 뉴올리언스 아웃폴 캐널과 오거스타 캐널은 길이가 같지 않습니다. 오를리언스 캐널은 약 3.6마일(5.8킬로미터) 길이이며 오거스타 캐널은 약 7마일(11.3킬로미터) 길이입니다.
#Your Judgement#: Yes
#Question#: What U.S Highway gives access to Zilpo Road, and is also known as Midland Trail?
#Question_Korean#: Zilpo Road에 접근할 수 있는 미국 고속도로는 무엇이며, 미들랜드 트레일(Midland Trail)로도 알려져 있나요?
#Answer#: U.S Highway 70
#Answer_Korean#: 미국 고속도로 70
#Your Judgement#: Yes

You are trying to translate the knowledge, question, and answer into a different language.
You are trying to determine if the answer is too general or too specific to answer the question at an appropriate level of specificity.
#Question#: What genre do Superheaven and Oceansize belong to?
#Question_Korean#: Superheaven과 Oceansize는 어떤 장르에 속하나요?
#Answer#: Superheaven and Oceansize belong to the rock genre.
#Answer_Korean#: Superheaven과 Oceansize는 록 장르에 속합니다.
#Your Judgement#: No
#Question#: What profession do Kōbō Abe and Agatha Christie share?
#Question_Korean#: 코보 아베(Kōbō Abe)와 아가사 크리스티(Agatha Christie)는 어떤 직업을 공유하나요?
#Answer#: Playwright.
#Answer_Korean#: 극작가
#Your Judgement#: No

You are trying to translate the knowledge, question, and answer into a different language.
You are trying to determine if the answer can be correctly inferred from the knowledge.
#Question#: Which band has more members, Muse or The Raconteurs?
#Question_Korean#: 뮤즈(Muse)와 더 래콘토어스(The Raconteurs) 중에서 더 많은 멤버를 가진 밴드는 무엇인가요?
#Answer#: Muse has more members than The Raconteurs.
#Answer_Korean#: 뮤즈는 더 래콘토어스보다 더 많은 멤버를 가지고 있습니다.
#Your Judgement#: Yes
#Question#: Which is currently more valuable, Temagami-Lorrain Mine or Meadowbank Gold Mine?
#Question_Korean#: 현재 더 가치 있는 것은 Temagami-Lorrain 광산인가요, Meadowbank 금 광산인가요?
#Answer#: Meadowbank Gold Mine, since Meadowbank Gold Mine is still producing gold and the TemagamiLorrain Mine has been inactive for years.
#Answer_Korean#: Meadowbank 금 광산입니다. Meadowbank 금 광산은 아직 금을 생산하고 있으며 TemagamiLorrain 광산은 수년간 활동하지 않았습니다.
#Your Judgement#: No

You should try your best to determine if the answer contains non-factual or hallucinated information according to the above hallucination types. The answer you give MUST be \"Yes\" or \"No\""."""

# QA_INSTURCTIONS = """I want you act as an answer judge. Given a question and an answer, your objective is to determine if the provided answer contains non-factual or hallucinated information. You SHOULD give your judgement based on the following hallucination types and the world knowledge.
#
# You are trying to determine if the answer misunderstands the question context and intention.
# #Question#: What is a rare breed of dog that was derived as a variant of Rat Terrier, Shiloh Shepherd dog or American Hairless Terrier?
# #Answer#: American Hairless Terrier
# #Your Judgement#: No
#
# You are trying to determine if there is a factual contradiction between the answer and the world knowledge. Some information in the answer might be fabricated.
# #Question#: Are the New Orleans Outfall Canals the same length as the Augusta Canal?
# #Answer#: No, the New Orleans Outfall Canals and the Augusta Canal are not the same length. The Orleans Canal is approximately 3.6 miles (5.8 kilometers) long while the Augusta Canal is approximately 7 miles (11.3 kilometers) long.
# #Your Judgement#: Yes
# #Question#: What U.S Highway gives access to Zilpo Road, and is also known as Midland Trail?
# #Answer#: U.S Highway 70
# #Your Judgement#: Yes
#
# You are trying to determine if the answer is too general or too specific to answer the question at an appropriate level of specificity.
# #Question#: What genre do Superheaven and Oceansize belong to?
# #Answer#: Superheaven and Oceansize belong to the rock genre.
# #Your Judgement#: No
# #Question#: What profession do Kōbō Abe and Agatha Christie share?
# #Answer#: Playwright.
# #Your Judgement#: No
#
# You are trying to determine if the answer can be correctly inferred from the knowledge.
# #Question#: Which band has more members, Muse or The Raconteurs?
# #Answer#: Muse has more members than The Raconteurs.
# #Your Judgement#: Yes
# #Question#: Which is currently more valuable, Temagami-Lorrain Mine or Meadowbank Gold Mine?
# #Answer#: Meadowbank Gold Mine, since Meadowbank Gold Mine is still producing gold and the TemagamiLorrain Mine has been inactive for years.
# #Your Judgement#: No
#
# You should try your best to determine if the answer contains non-factual or hallucinated information according to the above hallucination types. The answer you give MUST be \"Yes\" or \"No\""."""

DIALOGUE_INSTRUCTIONS = """I want you act as a response judge. Given a dialogue history and a response, your objective is to determine if the provided response contains non-factual or hallucinated information. You SHOULD give your judgement based on the following hallucination types and the world knowledge.

You are trying to determine if the true entity in the response is replaced with a highly similar entity.
#Dialogue History#: [Human]: Could you recommand movies similar to The Dark Knight? [Assistant]: The sequel to Batman Begins is The Dark Knight. [Human]: Okay. Who is the director of The Dark Knight and any other movies from him not related to Batman?
#Response#: Christopher Nolan was the director. He also directed insomnia and inception.
#Your Judgement#: No
#Dialogue History#: [Human]: Could you recommand movies similar to The Dark Knight? [Assistant]: The sequel to Batman Begins is The Dark Knight. [Human]: Okay. Who is the director of The Dark Knight and any other movies from him not related to Batman?
#Response#: Steven Spielberg was the director. He also directed insomnia and inception.
#Your Judgement#: Yes

You are trying to determine if the true entity in the response is replaced with a dissimilar entity.
#Dialogue History#: [Human]: Could you recommand movies similar to The Dark Knight? [Assistant]: The sequel to Batman Begins is The Dark Knight. [Human]: Okay. Who is the director of The Dark Knight and any other movies from him not related to Batman?
#Response#: Christopher Nolan was the director. He also directed insomnia and inception.
#Your Judgement#: No
#Dialogue History#: [Human]: Could you recommand movies similar to The Dark Knight? [Assistant]: The sequel to Batman Begins is The Dark Knight. [Human]: Okay. Who is the director of The Dark Knight and any other movies from him not related to Batman?
#Response#: Batman Begins was the director. He also directed insomnia and inception.
#Your Judgement#: Yes

You are trying to determine if the true entity in the response is replaced with a dissimilar entity in a different entity type.
#Dialogue History#: [Human]: Could you recommand movies similar to The Dark Knight? [Assistant]: The sequel to Batman Begins is The Dark Knight. [Human]: Okay. Who is the director of The Dark Knight and any other movies from him not related to Batman?
#Response#: Christopher Nolan was the director. He also directed insomnia and inception.
#Your Judgement#: No
#Dialogue History#: [Human]: Could you recommand movies similar to The Dark Knight? [Assistant]: The sequel to Batman Begins is The Dark Knight. [Human]: Okay. Who is the director of The Dark Knight and any other movies from him not related to Batman?
#Response#: United States of America was the director. He also directed insomnia and inception.
#Your Judgement#: Yes

You should try your best to determine if the response contains non-factual or hallucinated information according to the above hallucination types. The answer you give MUST be \"Yes\" or \"No\""."""

SUMMARIZATION_INSTRUCTIONS = """I want you act as a summary judge. Given a document and a summary, your objective is to determine if the provided summary contains non-factual or hallucinated information. You SHOULD give your judgement based on the following hallucination types and the world knowledge.

You are trying to determine if the summary is factual but some information cannot be directly inferred or entailed from the document.
#Document#: The panther chameleon was found on Monday by a dog walker in the wooded area at Marl Park. It had to be put down after X-rays showed all of its legs were broken and it had a deformed spine. RSPCA Cymru said it was an "extremely sad example of an abandoned and neglected exotic pet". Inspector Selina Chan said: "It is a possibility that the owners took on this animal but were unable to provide the care he needs and decided to release him to the wild. "We are urging potential owners of exotic animals to thoroughly research what is required in the care of the particular species before taking one on. "Potential owners need to make sure they can give their animal the environment it needs and they have the facilities, time, financial means and long-term commitment to maintain a good standard of care, as required under the Animal Welfare Act 2006." She added it was illegal to release non-native species into the wild.
#Summary#: A chameleon that was found in a Cardiff park has been put down after being abandoned and neglected by its owners.
#Your Judgement#: Yes

You are trying to determine if there exists some non-factual and incorrect information in the summary.  
#Document#: The city was brought to a standstill on 15 December last year when a gunman held 18 hostages for 17 hours. Family members of victims Tori Johnson and Katrina Dawson were in attendance. Images of the floral tributes that filled the city centre in the wake of the siege were projected on to the cafe and surrounding buildings in an emotional twilight ceremony. Prime Minister Malcolm Turnbull gave an address saying a "whole nation resolved to answer hatred with love". "Testament to the spirit of Australians is that with such unnecessary, thoughtless tragedy, an amazing birth of mateship, unity and love occurs. Proud to be Australian," he said. How the Sydney siege unfolded New South Wales Premier Mike Baird has also announced plans for a permanent memorial to be built into the pavement in Martin Place. Clear cubes containing flowers will be embedded into the concrete and will shine with specialised lighting. It is a project inspired by the massive floral tributes that were left in the days after the siege. "Something remarkable happened here. As a city we were drawn to Martin Place. We came in shock and in sorrow but every step we took was with purpose," he said on Tuesday.
#Summary#: Crowds have gathered in Sydney's Martin Place to honour the victims of the Lindt cafe siege, one year on.
#Your Judgement#: No

You are trying to determine if there is a factual contradiction between the summary and the document.
#Document#: Christopher Huxtable, 34, from Swansea, had been missing since the collapse in February. His body was found on Wednesday and workers who carried out the search formed a guard of honour as it was driven from the site in the early hours of the morning. Ken Cresswell, 57, and John Shaw, 61, both from Rotherham, remain missing. The body of a fourth man, Michael Collings, 53, from Brotton, Teesside, was previously recovered from the site. Swansea East MP Carolyn Harris, who has been involved with the family since the incident, said they still did not know all the facts about the collapse. She said: "I feel very sad. My heart and my prayers go out to the family who have waited desperately for Christopher's body to be found. They can finally have closure, and say goodbye to him and grieve his loss. "But let's not forget that there's two other families who are still waiting for their loved ones to be returned." The building was due for demolition when it partially collapsed in February.
#Summary#: The body of a man whose body was found at the site of the Swansea Bay Power Station collapse has been removed from the site.
#Your Judgement#: Yes

You should try your best to determine if the summary contains non-factual or hallucinated information according to the above hallucination types. The answer you give MUST be \"Yes\" or \"No\""."""


def doc_to_text_qa(doc: dict[str, str]) -> str:
    # prompt = instruction + "\n\n#Question#: " + question + "\n#Answer#: " + answer + "\n#Your Judgement#:"
    doc_text = QA_INSTURCTIONS_MT + "\n\n#Knowledge: " + doc["knowledge"] + "\n#Question#: " + doc["question"] + "\n#Answer#: " + doc["answer"] + "\n#Your Judgement#:"
    return doc_text


def doc_to_text_dialogue(doc: dict[str, str]) -> str:
    # prompt = instruction + "\n\n#Dialogue History#: " + dialog + "\n#Response#: " + response + "\n#Your Judgement#:"
    doc_text = DIALOGUE_INSTRUCTIONS + "\n\n#Knowledge: " + doc["knowledge"] + "\n#Dialogue History#: " + doc["dialogue_history"] + "\n#Response#: " + doc["response"] + "\n#Your Judgement#:"
    return doc_text


def doc_to_text_summarization(doc: dict[str, str]) -> str:
    # prompt1 = instruction + "\n\n#Document#: " + document
    # prompt2 = "\n#Summary#: " + summary + "\n#Your Judgement#:"
    doc_text_1 = SUMMARIZATION_INSTRUCTIONS + "\n\n#Document#: " + doc["document"]
    doc_text_2 = "\n#Summary#: " + doc["summary"] + "\n#Your Judgement#:"
    doc_text = doc_text_1 + doc_text_2
    return doc_text


def doc_to_target(doc: dict[str, str]) -> str:
    return doc['hallucination']


def compute_metrics(gold_answer: str, prediction: str) -> dict[str, float]:
    is_correct = True

    if ("Yes" in prediction and "No" in prediction) or ("Yes" not in prediction and "No" not in prediction):
        is_correct = False
    elif "Yes" in prediction:
        prediction = "yes"
    elif "No" in prediction:
        prediction = "no"

    is_exact = gold_answer == prediction
    # is_exact = "yes" == prediction

    # real
    res = {"acc": 1.0 if (is_correct and is_exact) else 0.0}



    return res


def process_results(doc: dict[str, str], results: list[str]):
    # results is e.g., ['Yes']
    gold_list = doc_to_target(doc)
    # gold_list is e.g., 'yes'
    prediction = results[0].strip().split("\n")[0]
    scores = compute_metrics(gold_list, prediction)
    return scores
