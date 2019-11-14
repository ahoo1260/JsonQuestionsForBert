import json

def getJsonInputForBert(questions, data,OUT_FILE_NAME):

    paragraphs=""
    no_questions = len(questions)
    for i in range(len(data)):
        print(paragraphs)
        paragraphs = paragraphs + "{\"context\":\"" + data[i] + "\",\"qas\":["

        for j in range(len(questions)):
            paragraphs=paragraphs+ "{\"question\":\"" + questions[j] + "\",\"id\":\"" + str((j+1) + i * no_questions) + "\" , \"is_impossible\": false },"\

        paragraphs=paragraphs[:-1]
        paragraphs=paragraphs+"]},"

    paragraphs = paragraphs[0:len(paragraphs) - 1]
    json_string = "{\"data\": [{\"title\": \"house\",\"paragraphs\": [" + paragraphs + "]}]}"

    print(json_string)

    jso = json.loads(json_string)

    with open(OUT_FILE_NAME, 'w') as outfile:
        json.dump(jso, outfile)
    return jso



def main():
    OUTPUT_FILE_NAME= "questionsJson.json"

    #any number of questions can be defined and should be inserted in a list of strings
    #questions=["question 1", "question 2", ..., "question N"]
    #example of two questions:
    questions=["where is paris?","who built Eiffel tower?"]


    #the documents that you are looking for the answers in them should be defined as list of strings
    # documents=["doc 1","doc 2","doc3",...,"doc N]
    #example of two documents:
    documents=["The Eiffel Tower was an inspiration for the Blackpool Tower in Blackpool, England, which proved that a tower "
          "could be a profitable tourist attraction. The Blackpool Tower was originally the idea of the Standard Contract"
          " and Debenture Corporation, based in the Isle of Man, who proposed the erection of two towers,"
          " one in Blackpool and one in the Isle of Man and sold shares to potential investors, including many prominent Blackpool families. ",
          "Paris (French pronunciation: ​[paʁi] (About this soundlisten)) is the capital and most populous city of France,"
          " with an area of 105 square kilometres (41 square miles) and an official estimated population of 2,140,526 "
          "residents as of 1 January 2019.[1] Since the 17th century, Paris has been one of Europe's major centres of finance,"
          " diplomacy, commerce, fashion, science, and the arts. The City of Paris is the centre and seat of government of the France,"
          " or Paris Region, which has an estimated official 2019 population of 12,213,364, or about 18 percent of the population of France."]

    getJsonInputForBert(questions,documents,OUTPUT_FILE_NAME)


if __name__ == "__main__":
    main()