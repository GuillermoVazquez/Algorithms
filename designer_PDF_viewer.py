
def designerPdfViewer(h, word):
    max = 0
    count = 0

    for letter in word:
        count+=1
        if h[ord(letter) - 97] > max:
            max = h[ord(letter) - 97]
    return max * count

if __name__ == '__main__':
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ,5 ,5 ,5 ,5, 5]
    word = "abc"
    print(designerPdfViewer(h,word))
