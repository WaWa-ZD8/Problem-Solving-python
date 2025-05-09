def designerPdfViewer(h, word):
    max_height = 0
    for i in word:
        index_num = ord(i) - ord("a")
        max_height = max(max_height, h[index_num])
        
    print(max_height * len(word))
        
if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
