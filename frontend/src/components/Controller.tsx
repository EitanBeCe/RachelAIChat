import { useState } from "react";
import Title from "./Title.tsx";

function Controller() {
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState<any[]>([]);

  const createBlobUrl = (data: any) => {};

  const handleStop = async () => {};

  return (
    <div className="h-screen overflow-y-hidden">
      <Title setMessages={setMessages}/>
      <div className="flex flex-col justify-between h-full overflow-y-scroll pb-96">
        Placeholer
      </div>
    </div>
  );
}

export default Controller;
