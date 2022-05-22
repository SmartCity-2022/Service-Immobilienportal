import React, { useEffect, useState } from "react";
import './App.css';
import { Flex, Box, Text, Button, Image, Link} from '@chakra-ui/react';

const Banner = ({purpose, title1, desc1, imageUrl, buttonText}) => (
  <Flex flexWrap="wrap" justifyContent="center" alignItems="center" m="10">
    <Image src={imageUrl} width={500} height={300} alt="banner"/>
    <Box p="5">
      <Text color="gray.500" fontSize="sm" fontWeight="medium">{purpose}</Text>
      <Text fontSize="3xl" fontWeight="bold">{title1}<br /></Text>
      <Text fontSize="lg" paddingTop="3" paddingBottom="3" color="gray.700">{desc1}</Text>
      <Button fontSize="xl" bg="blue.300" color="white">
        <Link href="#">{buttonText}</Link>
      </Button>
    </Box>
  </Flex>
)

const App = () => {
  return (
    <div>
      <Banner
       purpose="Free housing"
       title1="Top Angebot der Woche"
       desc1="It's free real estate"
       buttonText="Explore"
       imageUrl="/images/house1.jpg"
       />
    </div>
  );
}

export default App;
