
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
    }
}


export default actions