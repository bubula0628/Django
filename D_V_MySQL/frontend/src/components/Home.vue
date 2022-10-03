<template>

    <div class="home">
        <img src="../assets/logo.png">
        <el-row display="margin-top:10px">
            <el-input v-model="input.bookName" placeholder="請輸入書名" style="display:inline-table; width: 30%; float:left"></el-input>
            <el-input v-model="input.bookAuthor" placeholder="請輸入書名" style="display:inline-table; width: 30%; float:left"></el-input>
            <el-button type="primary" @click="addBook()" style="float:left; margin: 2px;">新增</el-button>
        </el-row>
        <p>{{input}}</p>
        <p>{{bookList}}</p>
        <el-table :data="bookList" style="width: 100%" border>
            <el-table-column prop="id" label="編號" min-width="100" />
            <el-table-column prop="bookName" label="書名" min-width="100" />
            <el-table-column prop="bookAuthor" label="作者" min-width="100" />
            <el-table-column prop="createTime" label="添加時間" min-width="100" />
        </el-table>
    </div>
</template>

<script>
    export default{
        name: "demo",
        data() {
            return {
                input: {
                    'bookName': "",
                    'bookAuthor':"",
                },
                //bookList: [{id: 1, bookName: 'phyger', bookAuthor: 'test-a', createTime:'test-time'}],
                bookList:[]
            }
        },
        mounted: function () {
            this.showBooks()
        },
        methods: {
            showBooks () {
                this.$axios.get('http://127.0.0.1:8000/api/books/')
                .then((response) => {
                    this.bookList = response.data
                    console.log(response.data)
                })
            },    
            addBook () {
                this.$axios.post(`http://localhost:8000/api/books/`, {'bookName': this.input.bookName, 'bookAuthor': this.input.bookAuthor})
                .then((response) => {
                    this.bookList = response.data
                    console.log(response.data)
 
                })
            }

        },
    }
  </script>
  
  <style>
    #app {
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
      margin-top: 60px;
    }
    </style>