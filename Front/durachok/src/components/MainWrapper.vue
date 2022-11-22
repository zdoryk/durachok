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
        <div v-if="playerActionName" class="action" id="take" @click="end_turn">{{playerActionName}}</div>
<!--        <div :style="{'visibility': 'hidden'}">{{// playerAction}}</div>-->
      </div>
    </div>
  </div>
</template>

<script>

import CardTable from "@/components/CardTable/CardTable";
import HandWithCards from "@/components/HandWithCards/HandWithCards";
import OpponentComponent from "@/components/Opponent";
import {mapActions, mapGetters} from "vuex";


export default {
  name: "MainWrapper",
  components: {OpponentComponent, CardTable, HandWithCards},
  data(){
    return{
      action_name: ''
    }
  },
  methods: {
    ...mapActions(['POST_PLAYER_CARD', 'GET_WORLD_INFO', 'GET_TABLE', 'ERASE_OLD_DATA', 'END_TURN']),
    end_turn(){
      // const action = this.playerActionName
      // const card = {
      //   card_rank: -1,
      //   card_suit: 'hearts'
      // }
      this.END_TURN(this.playerActionName)
    }
  },
  // created() {
  //   this.GET_INITIAL()
  // },
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
        // Тут можно сделать так чтобы кнопку было видно только при определеных условиях например если у нас нет карт чтобы подкинуть
        // if (this.cards.some(card => this.$store.state.used_card_ranks.includes(card.card_rank) ||
        //     this.$store.state.used_card_ranks.length === 0)){
        //   // console.log('Attack')
        //   return "Attack"
        // }
        return "Pass"
      }
      if (this.player.player_state === 2){
          // Тут можно сделать так чтобы кнопку было видно только при определеных условиях например если у нас нет карт чтобы одбится
          //
          // let matching_cards = this.cards.filter(card => card.card_suit === this.lastBottomCard.card_suit && card.card_rank > this.lastBottomCard.card_rank)
          // if (matching_cards.length) {
          //   // console.log(1)
          //   return ""
          // }
          return "Take"
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


  .action{
    /*width: 50%;*/
    /*height: 70px;*/
    /*font-size: 32px;*/
    border: none;
    border-radius: 4px;
    color: white;
    background-color: #6c97e2;
    box-shadow: 0 5px 0px 1px #5c7ab3;
    transition:  150ms ;
    cursor: pointer;
  }

  .action:hover{
    background-color: #7cacff;
    box-shadow: 0 5px 2px 1px #6f94dd;
  }

</style>
