let getters = {
    CARDS(state){
        return state.cards
    },
    BOTTOM_CARDS(state){
        return state.cards_on_bot
    },
    CARD_VALUES(state){
        return state.card_values
    }


}

export default getters;