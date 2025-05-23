import datasets
import re

few_samples = """
작성일: 20150819\n문서: 구글이 6개 아프리카 국가에 새 ‘안드로이드 원’ 스마트폰을 출시한다.\n\nAP통신에 따르면 구글은 18일(현지시간) 인피닉스(Infinix) 사가 제작하는 새 스마트폰 ‘핫 2(Hot 2)’ 모델을 새로 출시했다. 
‘핫 2’ 모델은 5인치 터치스크린과 1.3GHz 쿼드코어 프로세서, 16GB의 저장공간 등 보급형 스마트폰에 걸맞는 사양을 갖췄다. 이번 ‘핫 2’ 모델은 구글이 작년부터 시작한 ‘안드로이드 원’ 프로젝트의 일환이다. 
‘안드로이드 원’은 전자제품을 사치품으로 취급하는 저개발국, 신흥국에 구글 레퍼런스 스마트폰 모델을 초저가로 보급하는 프로젝트다.
구글은 이 모델을 나이지리아, 가나, 케냐 등 6개 아프리카 국가에서 판매한다. 안드로이드 원 프로젝트가 아프리카 지역을 겨냥하는 것은 구글 역사상 처음 있는 일이다. 
구글은 안드로이드 원 기기를 작년 인도 시장에서 처음 선보인 이래 지금까지 방글라데시, 미얀마 등 아시아 지역에서만 판매해 왔다.
다른 안드로이드 원 기기처럼 이번 모델도 87달러(한화 약 10만원)에서 98달러 사이의 저렴한 가격에 팔리고 있다. 
현지 반응은 매우 긍정적이다. ‘핫 2’를 온라인으로 판매 중인 웹사이트에서 이 모델은 출시 당일인 화요일 바로 품절됐다. 
스마트폰 전문 사이트 GSM아레나는 “인피닉스가 ‘핫 2’를 통해 아프리카에서 가장 뜨겁고 빠르게 성장하는 스마트폰 브랜드가 됐다”며 놀라움을 표시했다.
안드로이드 원 외에 구글은 저개발국, 신흥국 인터넷 유저층을 두텁게 만들기 위한 여러 프로젝트를 추진 중에 있다. 해당 지역 인터넷 사용자 수를 늘려 장기적으로 
자사 제품과 서비스를 판매할 새로운 시장을 확보하려는 의도다. 우간다 수도 캄팔라에 광섬유 케이블망을 설치해 준 것이 이 같은 일환에서 추진된 대표적인 사업이다.\n주어진 문서를 통해 파악할 수 있는 내용에 해당하는 문장을 선택하시오. 단, 정답 문장은 여러 개 존재할 수 있다.\n
2. 구글은 아프리카 시장을 처음으로 겨냥하여 안드로이드 원 프로젝트를 진행했다. 

작성일: 20210902\n문서: 최근 10여년간 ‘줄기세포’만큼 기대와 실망, 환호와 탄식이 교차한 단어는 없을 것이다. ‘불치병의 치료’라는 인류 공동의 숙원이 걸려 있기 때문이다.
적게는 1000만원에서 1억원이 넘는 치료비용이 들어가지만 근원치료가 가능하고 대체재가 없다는 점에서 글로벌 줄기세포 시장 규모는 꾸준히 증가하고 있다. 기업들의 투자도 이어지고 있다. 
지난해 하반기 세포치료와 유전자치료, 조직공학치료 등의 연구개발을 지원하는 ‘첨단재생의료법’이 발효되고 과기정통부와 보건복지부 및 산하연구기관이 협력하는 ‘범부처 재생의료기술 개발사업단’이 발족했다. 
제도적 지원이 기틀을 갖추면서 줄기세포의 특성을 활용한 다양한 치료법과 신약 개발이 활발하게 진행되고 있다. 가장 주목받는 것 중 하나가 혈관재생 세포를 활성화하는 줄기세포 치료제다. 
요체는 인체에 극히 소량만 존재하는‘혈관내피전구세포(EPC, Endothelial Progenitor Cells)’다. 
지구 토양에서 함유량이 극히 적지만 전세계 IT산업의 사활을 좌우하는 희토류(Rare Earth Element)에 비견될 수 있다. 한번 막히거나 손상된 혈관은 복구 불가능하다는 것이 의료상식으로 돼 있다. 
혈관 손상에 따른 심근경색, 부정맥, 협심증, 뇌졸중 등 이른바 ‘허혈성 혈관질환’으로 인한 사망이 세계적으로도 가장 많은 비중을 차지한다. 
EPC를 통해 혈관을 재생시키는 치료법에 기대가 모아지는 이유다. 개발과 상용화를 주도하는 유스바이오글로벌(YBG) 유승호 대표를 만났다. 유 대표는 서울대에서 보건학 석사와 의학박사 학위를 받았다. 
15년간 다국적 바이오 메디칼 기업에 근무하며 아시아 10여개국에서 경험을 쌓았다. 희귀난치성 질환으로 고통 받는 환자들에게 희망을 주기 위해 YBG를 설립했다. 
Q. EPC를 이용한 혈관 치료법에 대해 조금 더 부연 설명해주시면 좋겠습니다. A. 인체 내에서 혈관재생에 특화된 세포가 바로 혈관내피전구세포, EPC입니다. 
너무 미미하다 보니 그 존재를 찾아내고 연구가 시작 된지 20년 밖에는 안됐죠. 저희가 개발한 X EPC, 즉 Xeno Free EPC는 사람이나 동물유래 인자가 없다는 뜻입니다. 
즉 천연물에서 유래한 기능강화 인자들을 첨가해 배양함으로써 손상된 혈관에 직접 작용하도록 한 것입니다. 
이를 통해 생물학적 활성을 획기적으로 증가시키며, 조직재생 및 혈관의 새로운 생성에 기여하는 새로운 형태의 줄기세포입니다. 
그동안의 EPC 배양에는 필수적으로 4~5가지 성장인자와 다수의 생화학적 인자를 포함해야 했습니다. 
배양조성물은 혈관내피전구세포의 혈관재생능력을 향상시키고 세포의 성장을 촉진하는 것은 물론, 다수의 성장인자 없이도 줄기세포의 기능을 오래 유지시킬 수 있다는 점에서 획기적이라 할 수 있습니다. 
X EPC 세포치료제의 원료로는 분만실에서 버려지는 제대혈을 산모의 동의를 받아 사용하기 때문에 체내에서 세포 채취시 환자들의 고통도 덜 수 있습니다. 
\n주어진 문서의 내용과 다르거나 불확실한 환각 문장을 고르시오. 단, 환각 문장은 여러 개 존재할 수 있다.\n
1. X-EPC 세포치료제는 동물유래 인자를 포함하고 있어 안전성에 대한 우려가 있다. 
4. 유스바이오글로벌(YBG)은 최근 인공지능(AI) 기술을 활용해 줄기세포 치료제를 개발하고 있다.
5. 유스바이오글로벌은 최근 미국 FDA로부터 X-EPC 세포치료제의 상용화 승인을 받았다.

작성일: 20210111\n문서: 한국행정학회는 1956년 설립됐다. 민간·시장·정부 간 관계를 규정짓는 규제와 거버넌스를 연구하는 학계 싱크탱크다. 지난 연말 이 학회에 이변이 있었다. 
사상 처음으로 여성 학회장을 선출한 것이다. 65년 만의 일이다. 신임 행정학회장 박순애 서울대 행정대학원 교수(56·사진)는 \"2G 시대의 무거운 갑옷을 껴입은 행정 현장을 바꾸겠다\"며 출사표를 냈다. 
왜일까. `레드 테이프(red tape)`와 `여성`을 키워드 삼아 최근 서울대에서 박 교수를 만났다. 
\"갓 부임했던 시기에 행정학 수업에서 `왜 공무원이 되려고 하냐`고 물었더니 맨 앞줄 학생이 `교수님 정말 몰라서 물어보세요? 권력을 가질 수 있잖아요`라고 하더라고요. 
공무원이 무소불위의 권한을 가졌을 때가 있었지만 이제 온 국민이 전문가예요. 그만큼 공무원 역량을 불신합니다.\"\n\n레드 테이프는 관료제 형식주의의 상징이다. 
어원은 공무원 규제 서류를 묶은 `붉은 끈`이다. 미국은 규제 철폐를 약속하며 레드 테이프 커팅식까지 벌였다. 한국은 어떤가. 3년간 증원된 공무원이 9만명이란 뉴스가 들린다. 
그런데도 행정 현장은 늘 변화에 뒤처진다. 멀리 가볼 것도 없다. 붉은 수돗물 사태, 정인이 사건만 봐도 보는 이는 갑갑해진다.
\"영화 `나, 다니엘 블레이크` 풍경은 한국과 유사해요. 목수 블레이크는 심장병으로 실업급여를 받아야 하는데, 컴퓨터를 다루지 못하는 그에게 공무원은 온라인 신청이 규정이라는 말만 반복합니다. 
행정 편의주의가 영화만의 일인가요. 국가에 맞는 운영체제(OS)부터 바꿔 끼워야 합니다.\"
완전히 새로운 국가적 OS가 그의 관심사다. \"가상화폐 근원에는 무(無)국가주의가 숨어 있어요. 국가 시스템이 몸에 맞지 않는다고 느끼는 사람이 늘어납니다. 
코로나19는 탈국가주의를 가속화할 겁니다.\" 관료의 개인 책임성 확보가 답이라고 그는 본다. \n\n고생과는 거리가 멀어 보이는 화려한 외모와 달리 가재도구에 `빨간 딱지`가 붙을 만큼 어려운 환경에서 자랐다고 한다. 
아버지 반대를 무릅쓰고 간신히 서울에 있는 대학에 진학했다. 연세대 행정학과를 나온 그는 지금 근무하고 있는 서울대 행정대학원에서 몇 안 되는 비서울대 출신이다. 
그 과정이 수월하지만은 않았을 것이다. \n\n\"아이가 셋이에요. 첫째 딸 데리고 박사 학위 받으러 미국에 갔을 때 수업과 연구원 생활을 병행하며 애 키우는 일이 어디 쉬웠겠어요. 
어린 딸을 야간수업에 데리고 가서 눈총을 받던 기억, 둘째 아이가 아파서 밤 꼬박 새우고 노무현 전 대통령 취임식에 생중계 방송을 하러 갔던 날도 기억나요.\"\n주어진 문서의 내용과 다르거나 불확실한 환각 문장을 고르시오. 단, 환각 문장은 여러 개 존재할 수 있다.\n
3. 박순애 교수는 두 아이를 키우며 박사 학위를 받기 위해 미국에 갔다.
4. 박순애 교수는 3G 시대의 무거운 갑옷을 껴입은 행정 현장을 바꾸겠다고 말했다.

위의 예시를 참고하여 타당한 아래의 문서와 지시에 따라 올바른 답을 선택하시오.
"""


# def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
#     def _process_doc(doc):
#         knowledge = "작성일: " + doc["date"].strip() + '\n' + "문서: " + doc["document"].strip()
#         instruction = doc["instruction"].strip()
#         choices = [f"{i}. {doc[str(i)]}" for i in range(1,6)]
#         choices_str = "\n".join(choices)
#
#         # cot = """환각 여부 및 사실성을 검증하는 과정에서 다른 정답 후보군과의 상관관계를 고려하고, 정답이라 생각하는 이유가 무엇인지 고려해서 답을 선택하라."""
#         gen_inst = """
#         앞 문장의 지시에 부합하는 선택지는 1로 표기하고, 아닌 경우 0으로 표기한다.
#         반드시 리스트 안에 0 또는 1로 표기하고, 다른 내용이 포함되어 있으면 안 된다.  e.g., `[1, 0, 1, 1, 0]`
#         """
#         out_doc = "\n" + knowledge + '\n지시:' + instruction + '\n' + gen_inst + "\n선택지: " + choices_str
#         return out_doc
#
#     return dataset.map(_process_doc)

def doc_to_text(doc: dict[str, str]) -> str:
    knowledge = "작성일: " + doc["date"].strip() + '\n' + "문서: " + doc["document"].strip()
    instruction = doc["instruction"].strip()
    choices = [f"{i}. {doc[str(i)]}" for i in range(1,6)]
    choices_str = "\n".join(choices)

    # cot = """환각 여부 및 사실성을 검증하는 과정에서 다른 정답 후보군과의 상관관계를 고려하고, 정답이라 생각하는 이유가 무엇인지 고려해서 답을 선택하라."""
    gen_inst = """
    앞 문장의 지시에 부합하는 선택지는 1로 표기하고, 아닌 경우 0으로 표기한다.
    반드시 List로 결과물을 반환하라. 다른 내용이 포함되어 있으면 안 된다.
    [생성 결과물의 예시]
    e.g., 
    정답: [1, 0, 1, 1, 0] 
    정답: [1, 0, 1, 1, 0] 
    정답: [1, 0, 1, 1, 0]
    """
    out_doc = "\n" + knowledge + '\n지시:' + instruction + '\n' + gen_inst + "\n선택지: " + choices_str + "\n정답: "
    return out_doc

def compute_metrics(gold_answer: list, prediction: str) -> dict[str, float]:
    is_correct = True
    pattern = r"\[\s*(\d+(?:,\s*\d+)*)\s*\]"
    pattern2 = r"^\d+(?:,\s*\d+)*"
    cleaned_result = re.sub(r"</s>+", "", prediction).strip()  # </s>를 모두 제거

    match = re.search(pattern, prediction)
    match2 = re.match(pattern2, cleaned_result)
    if match:
        pred_list = [int(n) for n in match.group(1).split(",")]
        is_exact = gold_answer == pred_list

    elif match2:
        cleaned_result = match2.group()
        pred_list = [int(num.strip()) for num in cleaned_result.split(",")]
        is_exact = gold_answer == pred_list

    else:
        is_correct = False

    # is_exact = "yes" == prediction
    # real

    res = {"acc": 1.0 if (is_correct and is_exact) else 0.0}

    return res

def doc_to_target(doc: dict[str, str]) -> str:
    gold_list = [0,0,0,0,0]
    for i in doc['label']:
        gold_list[i] = 1

    return gold_list

def process_results(doc: dict[str, str], results: list[str]):
    # results is e.g., ['Yes']
    gold_list = doc_to_target(doc)
    # gold_list is e.g., 'yes'
    prediction = results[0].strip().split("\n")[0]
    scores = compute_metrics(gold_list, prediction)

    return scores