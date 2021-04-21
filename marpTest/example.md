---
marp: true
theme: default
# theme: gaia
# theme: uncover

# paginate: true

# size: 4:3
# size: 16:9

# header: 我是頁頭
# footer: 我是頁尾

# style: |
#   h1 {
#     text-align: end;color: blue;padding-right: 180px;font-size:100px
#   }

---
<!-- _backgroundColor: black -->
<!-- _class: invert -->
新頁面

---
# 設定Title

- 這是內文1
  - 內文A
    * 內文甲 
    * 內文乙 
  - 內文B
    * 內文丙  
- 這是內文1

---
# h1
## h2
### h3
#### h4
- **粗體**
- ~~刪除~~
- `區塊`
- *斜體*

---

- emoji: :spades: :hearts::diamonds::clubs::blush:
- Table: 

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| Text     | Text     | Text     |
| Text     | Text     | Text     |
| Text     | Text     | Text     |

> 我是引文

---
```C
int* sortArrayByParity(int* A, int ASize, int* returnSize){
    int *B;
    B=malloc(ASize*sizeof(int));
    int i,j=0,k=ASize-1;
    for(i=0;i<ASize;i++){
        if(A[i]%2!=0){
            B[k]=A[i];
            k--;
        }else{
            B[j]=A[i];
            j++;
        }
    }
    returnSize=ASize;
    return B;
}
```

---
```python
def duplicateZeros(arr):
    zero_index = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_index.append(i)
    for i in range(len(zero_index)):
        arr.insert(zero_index[i]+i, 0)
    new_length= len(arr)-len(zero_index)
    arr = arr[:new_length]
```

---
# 圖片

![bg](https://pic.pimg.tw/hakunafamily/1583488262-1704187650_n.png)

---
# 圖片

![bg brightness:0.3](https://pic.pimg.tw/hakunafamily/1583488262-1704187650_n.png)

---
# 圖片

![bg opacity:0.3](https://pic.pimg.tw/hakunafamily/1583488262-1704187650_n.png)

---
# 請提拔我
<!-- _backgroundColor: yellow -->
<!-- color: red -->

![bg left:70%](https://pic.pimg.tw/hakunafamily/1583488262-1704187650_n.png)