
import axios from "axios";


let actions = {
    THROW_CARD_ACTION({commit}, card){
        commit('THROW_CARD', card);
    },

    DEFEND_WITH_CARD_ACTION({commit}, card){
        console.log(card)
        commit("DEFEND_WITH_CARD", card)
    },

    SET_USED_CARD_RANKS_ACTION({commit}, card){
        console.log('hi')
        commit("SET_USED_CARD_RANKS", card)
    },

    SET_NEW_INDEXES_ACTION({commit}){
        console.log("indexes")
        commit("SET_NEW_INDEXES")
    },

    DELETE_CARD_FROM_HAND({commit}, card){
        commit("DELETE_CARD_FROM_HAND", card)
    },

    async GET_INITIAL(){
        return axios('http://127.0.0.1:8000/initial/', {
            method: "GET",
            // headers: {'X-Requested-With': 'XMLHttpRequest'},
        })
            .then((data) => {
                // commit("DELETE_CARD_FROM_HAND")
                console.log(data.data.data)
                return data;
            })
            .catch((error) => {
                console.log(error);
                return error;
            })
    },
}


export default actions
