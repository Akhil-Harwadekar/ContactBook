<template>
   <div class="numDisplay">
    <input id="phnum" v-model="num" maxlength="10">
    </div> <hr/>
    <div class="keys">
        <div class="row keybtn">
            <button v-on:click="readnum(7)" class="btn btn-dark">7</button>
            <button v-on:click="readnum(8)" class="btn btn-dark">8</button>
            <button v-on:click="readnum(9)" class="btn btn-dark">9</button>
        </div><br/>
        <div class="row keybtn">
            <button v-on:click="readnum(4)" class="btn btn-dark">4</button>
            <button v-on:click="readnum(5)" class="btn btn-dark">5</button>
            <button v-on:click="readnum(6)" class="btn btn-dark">6</button>
        </div><br/>
        <div class="row keybtn">
            <button v-on:click="readnum(1)" class="btn btn-dark">1</button>
            <button v-on:click="readnum(2)" class="btn btn-dark">2</button>
            <button v-on:click="readnum(3)" class="btn btn-dark">3</button>
        </div><br/>
        <div class="row keybtn">
            <button v-on:click="readnum('+')" class="btn btn-light">+</button>
            <button v-on:click="readnum(0)" class="btn btn-dark">0</button>
            <button v-on:click="readnum('-')" class="btn btn-light">-</button>
        </div><br/>
    </div>
    <button type="submit" class="btn btn-success" v-on:click="sendnum()" id="addContactbtn">Add to Contact</button>
    <button type="reset" class="btn btn-danger" id="cancelbtn"><a href="http://localhost:8080/">Cancel</a></button>
</template>

<script>
var arraynum = [];
var joinn;
export default {
    name:'DialPad',
    data(){
        return{
            num:''
        }
    },
    methods:{
        readnum(num){
            arraynum.push(num);
            var arrayStr = arraynum.toString();
            var splitt=arrayStr.split(',')
            joinn=splitt.join('');
            for(var i=0; i<arraynum.length; i++){
                document.getElementById('phnum').value=' +91-'+joinn;
            }        
        },
        sendnum(){
            var phsplit = document.getElementById('phnum').value;
            document.getElementById('readonlynum').value = phsplit;
            this.num = null
        }
    }
}
</script>

<style scoped>
.numDisplay > input{
    margin-top: 15%;
    font-size: 3.5em;
    margin-bottom: 3%;
    font-weight: 400;
    padding-right: 5%;
    border-radius: 20px;
    box-shadow: 1px 1px 5px black;
    width: 100%;
    border: none;
    outline: none;
}
.keybtn{
    padding-left: 18%;
}
.keybtn > button {    
    margin-right: 10%;
    width: 20%;
    height: 8vh;
    font-size: 2em;
}
#addContactbtn,#cancelbtn{
    margin-left: 23%;
    margin-bottom: 3%;
    height: 6vh;
    font-size: 1.2em;
    width: 10vw;
}
#cancelbtn{
    margin-left: 56%;
    margin-top: -17%;
    width: 9vw;
}
#cancelbtn > a{
    color: white;
    text-decoration: none;
}
</style>