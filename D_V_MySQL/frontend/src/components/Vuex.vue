<template>
  <a href="/">
  <el-button  type="primary"  style="float:center; margin: 2px;">返回Home</el-button>
  </a>
  <div>
<p>
<h3>locoalStorage </h3>
{{ bookList }}
</p>
</div>

<div>
<p>
<h3>Vuex </h3>
{{ $store.state.book_lists}}
</p>
</div>

<hr>
<div class="hello">
<h1>{{ $store.state.count }}</h1>
<button @click="addclick(1)">+</button>
<button @click="reduceclick(1)">-</button>

<div>非同步作業</div>
<div>
<button @click="async_add(3)">非同步增加</button>
<button @click="async_reduce(3)">非同步減少</button>
</div>
<h1>我是getters{{ count }}</h1>
</div>

</template>

<script>
import { mapMutations, mapActions, mapGetters } from "vuex";
export default {
  data: function () {
    return {
      bookList: localStorage.getItem("book_lists"),
    };
  },

  name: "HelloWorld",
  methods: {
    ...mapMutations({
      addclick: "mutationAdd",
    }),
    //addclick(n){
    //  this.$store.commit('mutationAdd',n);
    //},
    ...mapMutations({
      reduceclick: "mutationReduce",
    }),
    //reduceclick(n){
    //this.$store.commit('mutationReduce',n);
    //},
    ...mapActions({
      async_add: "actionsAdd",
    }),
    //async_add(n){
    //  this.$store.dispatch('actionsAdd',n)
    //},
    ...mapActions({
      async_reduce: "actionsReduce",
    }),
    //async_reduce(n){
    //  this.$store.dispatch('actionsReduce',n)
    //}
  },
  computed: {
    ...mapGetters({
      count: "getCount",
    }),
    //count(){
    //  return this.$store.getters.getCount
    //}
  },
};
</script>

