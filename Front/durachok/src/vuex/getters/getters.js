let getters = {
    CARDS(state){
        return state.cards
    },
    BOTTOM_CARDS(state){
        return state.cards_on_bot
    },
    TOP_CARDS(state){
        return state.cards_on_top
    },
    CARD_VALUES(state){
        return state.card_values
    },
    PLAYER(state){
        return state.player
    }


}

export default getters;