<template>
  <div class="opponent">
    <img class="user" src="../assets/user.png" alt="">
    <div class="opponent-hand">
      <div class="opp-cards">
        <div
            class="opp-card"
            v-for="n in this.opponent_cards_amount"
            :key="n"
        ></div>
      </div>
      <div class="cards_amount">{{this.opponent_cards_amount}} cards</div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "OpponentComponent",
  data(){
    return{
    }
  },
  computed: {
    ...mapGetters({
      opponent_cards_amount: 'OPPONENT_CARDS_AMOUNT'
    })
  }

}
</script>

<style scoped lang="scss">

@import "src/assets/style";

  .opponent{
    width: $hand-width;
  }

  .user{
    height: 70px;
    margin-bottom: 10px;
  }

  .opponent-hand{
    //padding: ;
    //border: 1px solid #2c3e50;
    border-radius: 5px;
    height: 10vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    max-width: $hand-width;
    margin-bottom: 5px;
  }

  .opp-cards{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }

  .opp-card{
    height: 25px;
    width: 15px;
    border: 2px solid #ffffff;
    border-radius: 4px;
    margin: 0 1px;
    background-color: blueviolet;
    box-shadow: 0 0 0px 2px #000000;
  }

  .cards_amount{
    margin-top: 5px;
  }



</style>
