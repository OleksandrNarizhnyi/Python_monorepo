### `$subtract` - вычитание двух значений

#### **Синтаксис:**  
```js
{ $subtract: [ <уменьшаемое>, <вычитаемое> ] }
```
- Принимает **только два аргумента**.

---

### ✅ **Примеры использования**  

#### 1️⃣ **Вычитание чисел**
```js
db.collection.aggregate([
  { $project: { 
  result: { $subtract: [10, 4] } 
    } 
  }
])
```



new Date().getFullYear()





---

#### 2️⃣ **Вычисление возраста**
```js
db.collection.aggregate([
  { 
    $project: { 
      age: { $subtract: [new Date().getFullYear(), "$birth_year"] } 
    }
  }
])
```





---





### `$unwind` — развернёт массив, создавая отдельный документ для каждого элемента массива.  
### ✅ **Синтаксис**
```js
{ $unwind: "$<массив>" }
```

---

### ✅ **Примеры использования**  

#### **1️⃣ Развернуть массив значений**
##### 📌 Исходные данные:
```js
db.students.insertMany([
  { _id: 1, name: "Alice", subjects: ["Math", "Physics", "Biology"] },
  { _id: 2, name: "Bob", subjects: ["History", "Literature"] },
  { _id: 3, name: "Charlie", subjects: [] }
])
```
##### 📌 Запрос:
```js
db.students.aggregate([
  { $unwind: "$subjects" }
])
```
##### ✅ **Результат:**
```js
{ "_id": 1, "name": "Alice", "subjects": "Math" }
{ "_id": 1, "name": "Alice", "subjects": "Physics" }
{ "_id": 1, "name": "Alice", "subjects": "Biology" }
{ "_id": 2, "name": "Bob", "subjects": "History" }
{ "_id": 2, "name": "Bob", "subjects": "Literature" }
```

---

#### **2️⃣ Развернуть массив с сохранением пустых значений**
📌 Если массив пуст (`[]`) или отсутствует, документ **исчезает**. Чтобы этого избежать, используйте `"preserveNullAndEmptyArrays": true`:  
```js
db.students.aggregate([
  { $unwind: { path: "$subjects", preserveNullAndEmptyArrays: true } }
])
```
✅ **Результат (Charlie теперь остался в выводе):**
```js
{ "_id": 1, "name": "Alice", "subjects": "Math" }
{ "_id": 1, "name": "Alice", "subjects": "Physics" }
{ "_id": 1, "name": "Alice", "subjects": "Biology" }
{ "_id": 2, "name": "Bob", "subjects": "History" }
{ "_id": 2, "name": "Bob", "subjects": "Literature" }
{ "_id": 3, "name": "Charlie", "subjects": null }
```

---
