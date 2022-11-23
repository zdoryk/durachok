
import axios from "axios";


let actions = {
    THROW_CARD_ACTION({commit}, card){
        commit('THROW_CARD', card);
    },

    DEFEND_WITH_CARD_ACTION({commit}, card){
        commit("DEFEND_WITH_CARD", card)
    },

    SET_USED_CARD_RANKS_ACTION({commit}, card){
        commit("SET_USED_CARD_RANKS", card)
    },

    SET_NEW_INDEXES_ACTION({commit}){
        commit("SET_NEW_INDEXES")
    },

    DELETE_CARD_FROM_HAND({commit}, card){
        commit("DELETE_CARD_FROM_HAND", card)
    },

    START_GAME({commit}) {
      commit("START_GAME")
    },

    ERASE_OLD_DATA({commit}){
      commit("ERASE_OLD_DATA_MUTATION")
    },

    async GET_INITIAL({commit, dispatch}){
        return axios('http://127.0.0.1:8000/initial/', {
            method: "GET",
            // headers: {'X-Requested-With': 'XMLHttpRequest'},
        })
            .then((data) => {
                // commit("DELETE_CARD_FROM_HAND")
                commit("INITIAL_SET_UP", data.data.data)
                if (data.data.data.player_state === false) {
                    dispatch('GET_TABLE_INITIAL')
                } else {
                    this.state.player.player_state = 1
                    this.state.player.is_player_active = true
                    dispatch('GET_TABLE')
                }
                return data;
            })
            .catch((error) => {
                console.log(error);
                return error;
            })
    },

    async GET_TABLE_INITIAL({commit}){
        return axios('http://127.0.0.1:8000/get_table/', {
            method: "GET",
            // headers: {'X-Requested-With': 'XMLHttpRequest'},
        })
            .then((data) => {
                console.log('Initial')
                console.log(data)
                console.log('---')
                commit('GET_TABLE_MUTATION', data.data.cards)
                commit('SET_PLAYER_DEFEND')
                return data;
            })
            .catch((error) => {
                console.log(error);
                return error;
            })
    },


    async GET_PLAYER_HAND({commit}){
        return axios('http://127.0.0.1:8000/get_player_hand/', {
            method: "GET",
            // headers: {'X-Requested-With': 'XMLHttpRequest'},
        }).then((data) => {
            // console.log('Player hand')
            // console.log(data)
            // console.log('---')
            commit('SET_PLAYER_HAND', data.data)
        })
    },

    async GET_TABLE({commit,dispatch}){
        return axios('http://127.0.0.1:8000/get_table/', {
            method: "GET",
            // headers: {'X-Requested-With': 'XMLHttpRequest'},
        })
            .then((data) => {
                // console.log('GET_TABLE_ACTION')
                // console.log(data.data)
                // console.log('---')
                if (data.data.cards.cards_on_bot.length === 0){
                    // console.log('No cards on bottom')
                    this.state.used_card_ranks = []
                    dispatch('GET_PLAYER_HAND')
                }
                commit('GET_TABLE_MUTATION', data.data.cards)
                return data;
            })
            .catch((error) => {
                console.log(error);
                return error;
            })
    },

    async GET_WORLD_INFO({commit}){
        return axios('http://127.0.0.1:8000/get_world_info/', {
            method: "GET",
            // headers: {'X-Requested-With': 'XMLHttpRequest'},
        })
            .then((data) => {
                // console.log(data)
                let info = JSON.parse(JSON.stringify(data.data.data))
                info.player_state = true
                commit('INITIAL_SET_UP', info)
                this.state.player.is_player_active = true
            })
    },

    async POST_PLAYER_CARD({dispatch, }, card){
        console.log('-----')
        console.log(this.state.player.player_state)
        axios.post('http://localhost:8000/player_card', card)
            .then( (data) => {
                // console.log(this.state)
                    if (this.state.player.player_state === 1) {
                        console.log('Player attacks with: ')
                        console.log(card)
                        console.log('Response: ')
                        console.log(data)
                        if (data.data === null){
                            // Player goes to defending
                            console.log('Bot took cards')
                            console.log('Player state = 2 (defending)')
                            this.state.player.player_state = 2
                            dispatch('GET_TABLE')
                            dispatch('GET_WORLD_INFO')
                            return 'Defend'
                        }
                        if ( typeof  data.data.bot_card !== 'undefined'){
                            dispatch('GET_TABLE')
                            dispatch('GET_WORLD_INFO')
                        }
                        if (data.data.bot_card !== '-1'){
                            console.log('Bot card:')
                            console.log(data.data.bot_card)
                            // console.log('---')
                            dispatch('SET_USED_CARD_RANKS_ACTION', data.data.bot_card)
                            dispatch('GET_TABLE')
                            dispatch('GET_WORLD_INFO')
                            return 'Push'
                        } else {
                            console.log('Bot took cards')
                            alert('Bot took cards')
                            dispatch('GET_TABLE')
                            dispatch('GET_WORLD_INFO')
                        }
                    } else {
                        console.log('Player defends with: ')
                        console.log(card)
                        console.log('Response: ')
                        console.log(data.data)
                        if (typeof data.data.data.bot_card !== 'undefined') {
                        // if (data.data.data !== null) {
                            // if (data.data.data.bot_card !== '-1') {
                                console.log('Bot card: ')
                                console.log(data.data.data.bot_card)
                                dispatch('SET_USED_CARD_RANKS_ACTION', data.data.data.bot_card)
                                dispatch('GET_TABLE')
                                dispatch('GET_WORLD_INFO')
                                this.state.player.is_player_active = true
                            // }
                            // else {
                            //     console.log('Bot card: ')
                            //     console.log(data.data.data.bot_card)
                            //     dispatch('GET_WORLD_INFO')
                            //     commit('GET_TABLE')
                            //     this.state.player.is_player_active = true
                            // }
                        } else {
                            console.log('Bot said: "Muck!"')
                            dispatch('GET_WORLD_INFO')
                            dispatch('ERASE_OLD_DATA')
                            alert('Bot said: "Muck!"')
                            // this.state.used_card_ranks = []
                            // this.state.cards_on_bot = []
                            // this.state.cards_on_top = []
                            this.state.player.player_state = 1
                            console.log("Now it's players turn")
                        }
                    }
                }
            );
    },
    async END_TURN({dispatch}, action){
        // console.log(this.state.player.player_state)
        // console.log(action)
        // axios.post('http://localhost:8000/player_card', card)
        axios.post('http://localhost:8000/player_card', {card_rank: '-1', card_suit: 'hearts'})
            .then( (data) => {
                if (action === 'Take'){
                    console.log('Player took cards')
                    this.state.player.player_state = 2
                } else {
                    console.log('Player said: "Mock!"')
                    this.state.player.player_state = 2
                }
                console.log('Bot response:')
                console.log(data)
                dispatch('GET_WORLD_INFO')
                dispatch('GET_TABLE')
                dispatch('ERASE_OLD_DATA')
            })
    }

}


export default actions
