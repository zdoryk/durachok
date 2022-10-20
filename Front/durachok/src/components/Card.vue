<template>
  <div id="v-card">
    <div class="text">
      {{card.card_suit}}
    </div>
    <div class="text">
      {{card.card_rank}}
    </div>
    <icon-component class="card" :name="this.cardPath" />

  </div>
</template>

<script>


import IconComponent from "@/components/Icon";
export default {
  name: "VCard",
  components: {IconComponent},
  props: {
    card: Object,
  },
  data(){
    return{
      // mySVG: require("../assets/cards/SVG-cards-1.3/5_of_hearts.svg")
    }
  },

  // created() {
  //   let path = "../assets/cards/SVG-cards-1.3/" + this.card.card_rank + "_of_" + this.card.card_suit + ".svg"
  //   this.mySVG = require(path)
  // },

  computed: {
    cardPath(){
      let path = "_" + this.card.card_rank + "_of_" + this.card.card_suit
      console.log(path)
      return path
    }

  }
}
</script>

<style scoped>
  .text {
    color: white;
    font-size: 30px;
  }

  .card {
    width: 100px;
    height: 150px;
  }


</style>