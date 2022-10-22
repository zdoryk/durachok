<template>
  <div class="v-card">
<!--    <icon-component :style="cssVars" class="card" :name="this.cardPath" />-->
    <img :style="cssVars" class="card" :src="icon" @click="throwCard"/>
  </div>
</template>

<script>


// import IconComponent from "@/components/Icon";
import * as icons from "@/assets/cards/SVG-cards-1.3";
import {mapActions, mapGetters} from "vuex";
// import getters from "@/vuex/getters/getters";
// import getters from "@/vuex/getters/getters";

export default {
  name: "VCard",
  components: {},
  props: {
    card: Object,
  },
  data(){
    return{
      // card_values: {
      //   6: "6",
      //   7: "7",
      //   8: "8",
      //   9: "9",
      //   10: "10",
      //   11: "jack",
      //   12: "queen",
      //   13: "king",
      //   14: "ace"
      // },
    }
  },

  methods: {
    ...mapActions([
      'THROW_CARD_ACTION', "DEFEND_WITH_CARD_ACTION",
      "SET_USED_CARD_RANKS_ACTION", "SET_NEW_INDEXES_ACTION",
      "DELETE_CARD_FROM_HAND"
    ]),

    parseProxy(proxy){
      return JSON.parse(JSON.stringify(proxy))
    },

    throwCard(){
      if ( this.$store.state.player.player_state === 1){ // State to attack
        if (this.$store.state.used_card_ranks.length === 0){ // If there are no cards on the table yet
          this.THROW_CARD_ACTION(this.card)
          // Then Request action to rest
          // Also changes state of player action from true to false
        } else {
          // Only ranks of cards that already on the table are okay
          if (this.$store.state.used_card_ranks.includes(this.card.card_rank)){ // if there is a card with the same rank
            // console.log(this.$store.state.used_card_ranks)
              this.THROW_CARD_ACTION(this.card)
          } else {
            alert("You cannot use this card try another one with one of these ranks: ( " + this.parseProxy(this.$store.state.used_card_ranks).map(rank => this.card_values[rank]) + " )")
            // this.THROW_CARD_ACTION(this.card)
          }
        }
      } else { // State to def
        let matching_cards = this.cards.filter(card => card.card_suit === this.lastBottomCard.card_suit && card.card_rank > this.lastBottomCard.card_rank)
        if(matching_cards.length === 0){
          // Only take because there is no cards with this suit and greater rank
          // Maybe it will be moved to HandWithCards component and putter to computed
        } else {
          if(matching_cards.includes(this.card)){
            console.log(matching_cards)
            this.DEFEND_WITH_CARD_ACTION(this.card)
            this.SET_USED_CARD_RANKS_ACTION(this.card)
            this.SET_NEW_INDEXES_ACTION()
            this.DELETE_CARD_FROM_HAND(this.card)
            this.$store.state.player.is_player_active = false
          }
        }
      }
    }
  },

  computed: {
    cardPath(){
      // if (this.card.card_rank > 10){
      //   return "_" + this.card_values[this.card.card_rank] + "_of_" + this.card.card_suit
      // }
      // else return "_" + this.card.card_rank + "_of_" + this.card.card_suit
      return "_" + this.card_values[this.card.card_rank] + "_of_" + this.card.card_suit
    },

    height_hover(){
      return this.card.card_height - 1
    },

    icon() {
      return icons[this.cardPath]
    },

    positionMultiplier() {
      return ((this.parseProxy(this.$store.state.table_size) - 70) / this.cards.length).toFixed(2)
    },

    cardPosition(){
      return this.card.card_index * this.positionMultiplier
    },

    ...mapGetters({
      cards: "CARDS",
      bottom_cards: "BOTTOM_CARDS",
      card_values: "CARD_VALUES"
    }),

    lastBottomCard(){
      return this.bottom_cards.at(-1)
    },

    cssVars(){
      return{
        "--height": this.card.card_height + 'px',
        "--height-hover": this.height_hover + 'px',
        "--translateX": "translateX(" + this.cardPosition + "px)",
        "--translate": "translate(" + this.cardPosition + "px, -10px)"
      }
    }

  }
}
</script>

<style scoped lang="scss">
  .text {
    color: white;
    font-size: 30px;
  }


  .card{
    height: var(--height);
    transition: 0.1s ease-in-out;
    transform: var(--translateX);
    bottom: 45px;
    position: absolute;
    cursor: pointer;
    //position: relative;
    //bottom: 520px;
  }

  .card:hover{
    //transform: translateY(-10px);
    transform: var(--translate);
  }



</style>