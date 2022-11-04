<template>
  <div id="main-wrapper">
    <div class="header">
      <opponent-component/>
    </div>
    <div class="body">
      <card-table/>
    </div>
    <div class="footer">
      <hand-with-cards/>
      <div class="player-action">
        <div v-if="playerActionName" class="action" id="take" >{{playerActionName}}</div>
<!--        <div :style="{'visibility': 'hidden'}">{{// playerAction}}</div>-->
      </div>
    </div>
  </div>
</template>

<script>

import CardTable from "@/components/CardTable/CardTable";
import HandWithCards from "@/components/HandWithCards/HandWithCards";
import OpponentComponent from "@/components/Opponent";
import {mapGetters} from "vuex";


export default {
  name: "MainWrapper",
  components: {OpponentComponent, CardTable, HandWithCards},
  data(){
    return{
      action_name: ''
    }
  },
  methods: {

  },
  computed: {
    ...mapGetters({
      player: "PLAYER",
      cards: "CARDS",
    }),

    lastBottomCard(){
      return this.$store.state.cards_on_bot.at(-1)
    },

    playerActionName(){
      if (this.player.player_state === 1){
        if (this.cards.some(card => this.$store.state.used_card_ranks.includes(card.card_rank))){
          console.log('Attack')
          return "Attack"
        }
        return "Pass"
      }
      if (this.player.player_state === 2){
        let matching_cards = this.cards.filter(card => card.card_suit === this.lastBottomCard.card_suit && card.card_rank > this.lastBottomCard.card_rank)
        if(matching_cards.length){
          // console.log(1)
          return ""
        }
        else {
          return "Take"
        }
      }
      return ''
      // FOR PURPOSES WHEN WE WILL HAVE MORE THAN 2 player_states
    }
  }
}
</script>

<style scoped>
  .header{
    height: 15%;
    display: flex;
    justify-content: center;
  }

  .body {
    height: 80%;
    display: flex;
    justify-content: center;
  }

  .footer{
    height: 5%;
    display: flex;
    justify-content: center;
    flex-direction: column;
  }

  .player-action{
    margin-top: 20px;
    display: flex;
    justify-content: center;
  }

  .action{
    border: 1px solid #0a2655;
    width: 100px;
    align-items: center;
    display: flex;
    justify-content: center;
    border-radius: 4px;
    cursor: pointer;
    transition: 0.2s ease-in-out;
    height: 30px;
  }

  .action:hover{
    box-shadow: 0 0 5px 0 #021934;
  }

</style>