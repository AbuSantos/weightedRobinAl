import { BsPlayCircle, BsPauseCircle } from 'react-icons/bs'

export default function Player({
  audioElem,
  isplaying,
  setisplaying,
  currentSong,
  setCurrentSong,
  songs,
}) {
  const PlayPause = () => {
    setisplaying(!isplaying)
  }

  return (
    <div>
      {isplaying ? (
        <BsPauseCircle onClick={PlayPause} />
      ) : (
        <BsPlayCircle onClick={PlayPause} />
      )}
    </div>
  )
}
