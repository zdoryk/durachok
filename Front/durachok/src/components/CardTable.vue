<template>
  <div id="card-table">
    <v-card v-bind:card="card_value"/>
  </div>
</template>

<script>

import VCard from "@/components/Card"

export default {
  name: "CardTable",
  components: {VCard},
  data(){
    return{
      card_value: {
        card_rank: 'queen',
        card_suit: 'diamonds',
      }
    }
  }
}
</script>

<style scoped>
  #card-table{
    background-color: #113911;
    height: 60vh;
    border-radius: 10px;
    margin: 5px;
    width: 60%;
  }


</style>