<template>
  <div id="card-table">
<!--    <v-card v-bind:card="card_value"/>-->
    <div class="first-column">
      <div class="card-deck">
        <div class="card-deck-amount">Deck: {{ this.deck_amount }} cards</div>
        <div class="card-deck-back card-deck"></div>
        <CardTableCard :card="this.trump" id="trump"/>
      </div>
    </div>
    <div class="second-column">
      <div class="play-zone">
        <div class="cards-on-bot">
          <CardTableCard
              v-for="(card_value, key, index) in this.bottom_cards"
              :key="index"
              v-bind:card="card_value"
              :top_or_bot="bot"
          />
        </div>
        <div class="cards-on-top">
          <CardTableCard
              v-for="(card_value, key, index) in this.top_cards"
              :key="index"
              v-bind:card="card_value"
              :top_or_bot="top"
          />
        </div>


      </div>
    </div>
    <div class="third-column">
      <div class="muck">
        <div class="card-deck-amount">Muck: {{ this.muck_amount }} cards</div>
        <div class="card-deck-back muck-card-back"></div>
      </div>
    </div>
  </div>
</template>

<script>

import CardTableCard from "@/components/CardTable/CardTableCard"
import {mapGetters} from "vuex";

export default {
  name: "CardTable",
  components: {CardTableCard},
  data(){
    return{
      top: "top",
      bot: "bot"
    }
  },

  computed: {
    cardsOnTop(){
      return this.$store.state.cards_on_top
    },

    cardsOnBot(){
      return this.$store.state.cards_on_bot
    },

    ...mapGetters({
      card_values: "CARD_VALUES",
      top_cards: "TOP_CARDS",
      bottom_cards: "BOTTOM_CARDS",
      deck_amount: "DECK_AMOUNT",
      muck_amount: "MUCK_AMOUNT",
      trump: "TRUMP"
    }),



  }
}
</script>

<style scoped lang="scss">

@import "../../assets/style";


  #card-table{
    background: radial-gradient(#177110, #164308);;
    height: 40vh;
    border-radius: 10px;
    margin: 5px;
    width: $table-width;
    padding: 0 20px;
    display: flex;
  }

  .first-column, .second-column, .third-column{
    width: 100%;
    height: 100%;
    //border: 1px solid #000000;
  }

  .first-column{
    flex: 1.3;
    display: flex;
    justify-content: center;
  }

  .second-column{
    flex: 5;
    padding: 10px;
  }

  .third-column{
    flex: 1;
  }

  .card-deck-amount{
    color: white;
    font-size: 16px;
    margin-top: 50px;
    margin-bottom: 15px;
  }

  .card-deck-back{
    background-color: blueviolet;
    height: 120px;
    width: 80px;
    border: 5px solid #ffffff;
    box-shadow: 0 0 0 3px #000000;
    border-radius: 5px;
    position: relative;
    bottom: 20px;
    left: 8px;
    rotate: 90deg;
    z-index: 2;
  }

  .card-deck {
    bottom: -30px;
  }

  .muck-card-back{
    rotate: 0deg;
    left: 0;
    bottom: -10px;
  }

  #trump{
    position: relative;
    bottom: 145px;
    z-index: 1;
  }


  .third-column{
    display: flex;
    //flex-direction: column;
    justify-content: center;
  }

  .play-zone{
    display: flex;
    flex-direction: column;
  }

  .cards-on-bot, .cards-on-top{
    display: flex;
    justify-content: space-evenly;
    //position: relative;
  }

  .cards-on-top{
    //top: 70px;
    z-index: 3;
    //left: 20px;
    //bottom: 50px;
  }

  .cards-on-bot{
    z-index: 2;
    //top: 70px;
    //bottom: 50px;
  }


</style>
