<template>
  <div :style=cssVars id="hand-with-cards">
    <div class="cards">
      <v-card
          class="card"
          v-for="(card_value, key, index) in this.cards"
          :key="index"
          v-bind:card="card_value"
      />
    </div>
  </div>
</template>

<script>

import VCard from "@/components/HandWithCards/Card"
// import getters from "@/vuex/getters/getters";

export default {
  name: "HandWithCards",
  data(){
    return{
      hand_height: 30
    }
  },

  methods: {
    // getters: {CARDS}
  },

  components: {VCard},
  computed: {
    height(){
      return 20
    },

    cards(){
      return this.$store.state.cards
    },

    cssVars(){
      return{
        "--hand-height": this.height + "vh",
        "--cards-height": this.height - 5 + "vh",
        "--cards-height-hover": this.height - 3 + "vh",
        "--opacity": this.isHandActive.opacity,
        "--pointer-events": this.isHandActive.pointer_events
      }
    },

    isPlayerActive(){
      return this.$store.state.player.is_player_active
    },

    isHandActive(){
      if (this.isPlayerActive === false) return {opacity: "0.6", pointer_events: "none"}
      return {opacity: "1", pointer_events: "auto"}
    }

  }

}
</script>

<style scoped lang="scss">

@import "../../assets/style";

  #hand-with-cards {
    width: 100%;
    display: flex;
    justify-content: center;
    opacity: var(--opacity);
    pointer-events: var(--pointer-events) ;
  }

  .cards{
    width: $table-width;
    height: 20vh;
    border: 1px solid #2c3e50;
    border-radius: 10px;
    margin: 5px;
    //display: flex;
    //justify-content: space-between;
    padding: 0 20px;
    align-items: center;
    transition: 0.2s ease-in-out;
  }


  .cards:hover{
    box-shadow: 0 0 20px 5px #021934;
  }

  .card{
    position: absolute;
  }

</style>