{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPX+INGpyPxEnSayD/Wg75k"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Z7lgfBxlWW17"
      },
      "outputs": [],
      "source": [
        "def getmax(lis):\n",
        "    return max(lis,key=len)\n",
        "\n",
        "lim=int(input(\"enter the limit of words u want to enter\"))\n",
        "lis1=[]\n",
        "for i in range(lim):\n",
        "    lis1.append(input(\"enter the words--\"))\n",
        "print(\"max of the given list is in the word----\", getmax(lis1))\n",
        "    "
      ]
    }
  ]
}