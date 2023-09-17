package seven;
import java.io.*;
import java.util.*;

public class checker {
    public static void main(String[] args) {
        if (args.length < 3) {
            System.out.println("请提供原文文件、抄袭版论文文件和答案文件的路径！");
            return;
        }

        String originalFile = args[0]; // 获取原文文件路径
        String plagiarizedFile = args[1]; // 获取抄袭版论文文件路径
        String answerFile = args[2]; // 获取答案文件路径

        try {
            String originalText = readFile(originalFile); // 从原文文件中读取文本内容
            String plagiarizedText = readFile(plagiarizedFile); // 从抄袭版论文文件中读取文本内容

            double similarity = calculateSimilarity(originalText, plagiarizedText); // 计算相似度

            writeResult(answerFile, similarity); // 将相似度结果写入答案文件
            System.out.println("相似度计算完成！请在对应的结果文件中查看计算结果"); // 输出计算完成的提示信息
        } catch (IOException e) {
            System.out.println("发生错误：" + e.getMessage()); // 输出错误信息
        }
    }

    private static String readFile(String filePath) throws IOException { // 从文件中读取文本内容的方法
        StringBuilder text = new StringBuilder(); // 用于存储读取的文本内容的 StringBuilder 对象
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) { // 使用 BufferedReader 读取文件内容
            String line; // 用于存储每行读取的文本
            while ((line = reader.readLine()) != null) { // 逐行读取文本内容，直到文件末尾
                text.append(line); // 将每行文本添加到 StringBuilder 对象中
            }
        }
        return text.toString(); // 将读取的文本内容转换为字符串并返回
    }

    private static double calculateSimilarity(String text1, String text2) { // 计算相似度的方法
        // 将文本分词，并去除重复词汇
        Set<String> words = new HashSet<>(); // 用于存储不重复单词的集合
        words.addAll(Arrays.asList(text1.split(""))); // 将原文的单词添加到集合中
        words.addAll(Arrays.asList(text2.split(""))); // 将抄袭版论文的单词添加到集合中

        // 构建文本向量
        int[] vector1 = new int[words.size()]; // 原文的词频向量
        int[] vector2 = new int[words.size()]; // 抄袭版论文的词频向量

        int index = 0; // 单词在向量中的索引
        Map<String, Integer> wordIndexMap = new HashMap<>(); // 用于存储单词和索引的映射关系的 Map
        for (String word : words) { // 遍历单词集合
            wordIndexMap.put(word, index); // 将单词和索引添加到映射关系中
            index++; // 索引递增
        }

        for (String word : text1.split("")) { // 遍历原文的单词
            int wordIndex = wordIndexMap.get(word); // 获取单词在向量中的索引
            vector1[wordIndex]++; // 增加对应索引位置的词频
        }

        for (String word : text2.split("")) { // 遍历抄袭版论文的单词
            int wordIndex = wordIndexMap.get(word); // 获取单词在向量中的索引
            vector2[wordIndex]++; // 增加对应索引位置的词频
        }

        // 计算余弦相似度
        double dotProduct = 0.0; // 点积
        double magnitude1 = 0.0; // 向量1的模
        double magnitude2 = 0.0; // 向量2的模

        for (int i = 0; i < vector1.length; i++) { // 遍历向量中的每个元素
            dotProduct += vector1[i] * vector2[i]; // 计算点积
            magnitude1 += Math.pow(vector1[i], 2); // 计算向量1的模的平方
            magnitude2 += Math.pow(vector2[i], 2); // 计算向量2的模的平方
        }

        magnitude1 = Math.sqrt(magnitude1); // 计算向量1的模
        magnitude2 = Math.sqrt(magnitude2); // 计算向量2的模

        if (magnitude1 == 0.0 || magnitude2 == 0.0) { // 处理模为0的情况，避免除以0的错误
            return 0.0;
        } else {
            return dotProduct / (magnitude1 * magnitude2); // 计算并返回相似度
        }
    }

    private static void writeResult(String filePath, double similarity) throws IOException { // 将结果写入文件的方法
        try (PrintWriter writer = new PrintWriter(new FileWriter(filePath))) { // 使用 PrintWriter 和 FileWriter 将结果写入文件
            writer.printf("相似度为：%.2f", similarity); // 将相似度结果格式化为保留两位小数，并写入文件
        }
    }
}
