<template>
  <main-wrapper  v-if="is_game_started === true"/>
  <div class="start-game-window" v-if="is_game_started === false">
    <div class="start">
      <button id="start-button" @click="start_game">
        Start Game
      </button>
    </div>
  </div>
</template>

<script>

import MainWrapper from "@/components/MainWrapper";
import {mapActions} from "vuex";

export default {
  name: 'App',
  components: {
    MainWrapper
  },
  computed: {
    is_game_started(){
      return this.$store.state.game_started
    }
  },
  methods: {
    ...mapActions(['START_GAME', 'GET_INITIAL']),
    start_game(){
      this.GET_INITIAL()
      this.START_GAME()
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 50px;
}

body{
  margin: 0;
}

.start-game-window{
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 90vh;
}

#start-button{
  width: 50%;
  height: 70px;
  font-size: 32px;
  border: none;
  border-radius: 4px;
  color: white;
  background-color: #6c97e2;
  box-shadow: 0 5px 0px 1px #5c7ab3;
  transition:  150ms ;
  cursor: pointer;
}

#start-button:hover{
  background-color: #7cacff;
  box-shadow: 0 5px 2px 1px #6f94dd;
}
</style>
