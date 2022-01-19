import React from "react";

interface Input {
  isTrue: boolean;
  func: () => void;
  text: string;
}

function ConditionalButton({ isTrue, func, text }: Input) {
  return (
    <button
      className={`hover:bg-blue-700 text-white mb-2 mr-2 py-2 text-sm px-4 rounded ${
        isTrue
          ? "bg-blue-500 hover:bg-blue-700 "
          : "bg-gray-400 hover:bg-gray-500"
      } `}
      onClick={() => {
        func();
      }}
    >
      {text}
    </button>
  );
}

export default ConditionalButton;
