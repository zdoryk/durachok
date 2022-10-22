
let mutations = {
    THROW_CARD: (state, card) => {
        // state.used_card_ranks.push(card.card_rank)
        // state.used_card_ranks = [...new Set(state.used_card_ranks)]

        state.cards_on_bot.push(card)

        // console.log(state.cards)
        // state.cards = JSON.parse(JSON.stringify(state.cards.filter(card_in_hand => card_in_hand.card_index !== card.card_index)))
        // for (let i = 0; i < state.cards.length; i++){
        //     state.cards[i].card_index = i
        // }

    },

    DEFEND_WITH_CARD: (state, card) => {
        state.cards_on_top.push(card)
    },

    SET_USED_CARD_RANKS: (state, card) => {
        console.log(card)
        state.used_card_ranks.push(card.card_rank)
        state.used_card_ranks = [...new Set(state.used_card_ranks)]
    },

    DELETE_CARD_FROM_HAND: (state, card) => {
        state.cards = JSON.parse(
            JSON.stringify(
                state.cards.filter(card_in_hand => card_in_hand.card_index !== card.card_index)))
    },

    SET_NEW_INDEXES: (state) => {
        for (let i = 0; i < state.cards.length; i++){
            state.cards[i].card_index = i
        }
    }
}




export default mutations