<template>
    <div class="container">
        <div class="row">
            <div class="col col-lg-6">
                <Entry />
            </div>
            <div class="col col-lg-6">
               <DialPad />
            </div>
        </div>
    </div>
</template>

<script>
import DialPad from './DialPad'
import Entry from "./Entry";

export default {
    name:'MainPage',
    components:{
        DialPad,
        Entry
    }
}
</script>