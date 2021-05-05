<template>
    <h1 class="display-2"> <img src="../assets/logo.png"> {{msg}}</h1>
    <MainPage />
</template>

<script>
import MainPage from "./MainPage";
export default {
    name:'NavPage',
    components: {
        MainPage
    },
    props:{
        msg:String,
    }
}
</script>

<style scoped>
    img{
        height: 15vh;
    }
</style>