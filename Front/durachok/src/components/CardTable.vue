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
        card_rank: '5',
        card_suit: 'hearts',
        // card_path: "src/assets/cards/SVG-cards-1.3/" + this.card_value.card_rank + "_of_" + this.card_value.card_suit + ".svg"
        card_path: this.$store.state.card.card_path
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