import bayes
def test():
    listOPosts, listClasses = bayes.loadDataSet()
    myVocabList = bayes.createVocabList(listOPosts)
    print(myVocabList)
    return
