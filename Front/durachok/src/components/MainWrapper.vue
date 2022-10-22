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
        <div id="action">Player action</div>
      </div>
    </div>
  </div>
</template>

<script>

import CardTable from "@/components/CardTable/CardTable";
import HandWithCards from "@/components/HandWithCards/HandWithCards";
import OpponentComponent from "@/components/Opponent";

export default {
  name: "MainWrapper",
  components: {OpponentComponent, CardTable, HandWithCards}

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

  #action{
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

  #action:hover{
    box-shadow: 0 0 5px 0 #021934;
  }

</style>