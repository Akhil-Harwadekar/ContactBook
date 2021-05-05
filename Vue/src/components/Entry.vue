<template>
    <h4 style="font-weight: 300; margin-bottom: 2.5%;">Personal Details</h4>
    <form @submit="sendData" method="POST">
        <div class="row">
            <div class="col">
                <input required class="form-control" name="fname" type="text" placeholder="First Name" v-model="FormData.fname">
            </div>
            <div class="col">
                <input class="form-control" type="text" placeholder="Last Name" v-model="FormData.lname">
            </div>
        </div><br/>
        <div class="row">
            <div class="col">
            <input required type="text" class="form-control" maxlength="10" id="readonlynum" placeholder="Contact Number" v-model="FormData.mobile">
            </div>
            <div class="col">
            <input class="form-control" type="email" placeholder="Email Id" v-model="FormData.email">
            </div>
        </div><br/>
        <button type="submit" class="btn btn-success float-right">Save Contact</button>
    </form>
    <br><br>
    <div class="container">
        <h3 style="font-weight: 300; margin-bottom: 3%;">My Contacts</h3>
        <div style="overflow-y: scroll; height: 34vh;">
            <ul class="list-group">
                <div class="container">
                    <p class="list-group-item list-group-item-primary" v-for="i in FormData.getinfos" :key="i.id"> 
                        <button class="btn btn-danger" @click="deleteNum(i.url)" style="margin-right:2%;"><ion-icon name="trash-outline"></ion-icon></button>
                          {{ i.fname }} {{ i.lname }} | {{ i.emailid }} | <b>{{ i.mobile }}</b>
                    </p>
                </div>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'Entry',
    data(){
        return{
            FormData : {
                fname:'',
                lname:'',
                mobile:'',
                email:'',
                name : [],
                getinfos:[],
            }
        }
    },
    methods:{
        sendData(){
            const params = new URLSearchParams();
            params.append('fname', this.FormData.fname);
            params.append('lname', this.FormData.lname);
            params.append('emailid', this.FormData.email);
            params.append('mobile', this.FormData.mobile);

            axios.post('http://127.0.0.1:8000/api/', params).then(() => {
                alert("Contact Added...")
                location.reload();
            });
        },
        getData(){
            axios.get(`http://127.0.0.1:8000/api/?format=json`).then(
                result => {
                    this.FormData.getinfos = result.data
                }
            )
        },
        deleteNum(numUrl){
            axios.delete(numUrl).then((res) => {
                alert('Number Deleted');
                location.reload()
                console.log(res+'Done');
            })
        }
    },
    mounted(){
        this.getData();
    }
}
</script>

<style scoped>
h4{
    margin-top: 9%;
}
</style>