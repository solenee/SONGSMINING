
STOPWORDS_EN="resources/stopwords_en.txt"
def formatSequence(filename, outputFile, cleaningFunction=None, sequenceEndChar=" .") :
  """ Remove points and empty lines then add a point at the end of each sequence """
  with open(filename, "r") as inputF:
    with open(outputFile, "w") as outputF : 
      for line in inputF : 
        if not (cleaningFunction is None) : line = cleaningFunction(line)
        if (line.strip() == "") : continue
        sequence = line.strip().replace(".", "")
        outputF.write(sequence+sequenceEndChar+"\n")
        
def removeStopwords(sequence) : 
  #TODO
  with open(STOPWORDS_EN, "r") as f:
    content = f.read()
    stopwords = content.split("\n")
  return sequence
  
def removePunctuation(word) :
  return word.replace("," ,"").replace("?", "").replace(";", "").replace(".", "").replace(":", "").replace("!", "").replace('\(', "").replace("\)", "")
