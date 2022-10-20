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

    }
  },

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