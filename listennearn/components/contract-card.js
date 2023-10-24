import Link from "next/link";
import styles from "../styles/Home.module.css";
import style from "../styles/NFt.module.css";
import { BsPlayCircle, BsPauseCircle } from "react-icons/bs";

import {
  MediaRenderer,
  useContract,
  useMetadata,
  useNFT,
  ThirdwebNftMedia,
} from "@thirdweb-dev/react";
import { useRef, useState, useEffect } from "react";
import Player from "./player/player";

export default function NFTCard(props) {
  const { contract } = useContract(props.contractAddress);
  const [isplaying, setisplaying] = useState(false);
  const [currentSong, setCurrentSong] = useState();

  const { data, isLoading, error } = useNFT(contract);
  const onPlaying = () => {
    const duration = audioElem.current.duration;
    const ct = audioElem.current.currentTime;

    setCurrentSong({
      ...currentSong,
      progress: (ct / duration) * 100,
      length: duration,
    });
  };

  const PlayPause = () => {
    setisplaying(!isplaying);
  };

  const audioElem = useRef();

  useEffect(() => {
    if (isplaying) {
      audioElem.current.play();
    } else {
      audioElem.current.pause();
    }
  }, [isplaying]);

  return (
    <Link href={props.href} className={styles.nftGridContainer}>
      {data && (
        <div>
          <ThirdwebNftMedia
            metadata={data.metadata.animation_url}
            controls={true}
            audioElem={audioElem}
            setisplaying={setisplaying}
          />
          {/* <audio
            src={data.metadata.animation_url}
            ref={audioElem}
            onTimeUpdate={onPlaying}
          /> */}
          {/* <Player
            isplaying={isplaying}
            setisplaying={setisplaying}
            audioElem={audioElem}
            currentSong={currentSong}
            setCurrentSong={setCurrentSong}
          /> */}
          <div className={styles.cardText}>
            <h2 className={styles.gradientText1}>{data.metadata.name}</h2>
            <p>{data.metadata.description}</p>
          </div>
        </div>
      )}
    </Link>
  );
}
