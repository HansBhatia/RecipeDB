import { useRouter } from 'next/router'

const Recipe = () => {
    const router = useRouter()
    const { recipe } = router.query // here we get a recipe string
    // now we search for the recipe in the db and get an object (RECIPE)
    // USE THE OBJECT PARAMS TO CREATE THE PAGE
    // ADD BOILER PLATE
    return <p>You searched for: {recipe}</p>
}

export default Recipe;
